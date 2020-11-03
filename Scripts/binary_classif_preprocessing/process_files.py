import os
from os import PathLike
from pathlib import Path
from time import time
from typing import List, Set

import numpy as np
from skimage.io import imsave

from load_data import load_images, load_masks
from windowify import windowify


def worker(
    args, accepted_labels: Set[str], uid: int, image_files: List[PathLike]
) -> None:
    output_directory: PathLike = args.output
    window_size: int = args.window_size
    overlap: int = args.overlap

    json_files: List[PathLike] = [
        Path(str(f).replace(".jpg", ".json")) for f in image_files
    ]
    images = load_images(filenames=image_files)
    image_shape = (images[0].shape[0], images[0].shape[1])
    masks = load_masks(
        filenames=json_files, image_shape=image_shape, accepted_labels=accepted_labels
    )[..., np.newaxis]

    # Highlights masked parts in red in the outputted chunks to help debug
    # images[..., :1][masks] = 255

    windows_images = windowify(
        masked_image_array=images, window_size=window_size, overlap=overlap
    )
    # The last dim of the windowed labels gets squeezed and consequently removed
    windows_labels = windowify(
        masked_image_array=masks, window_size=window_size, overlap=overlap
    )[..., np.newaxis]
    # windows_images = images
    # windows_labels = images.astype(np.bool)

    # Collapses the batch, chunk_x and chunk_y dimensions into a single one
    windows_images = windows_images.reshape((-1, *windows_images.shape[-3:]))
    windows_labels = windows_labels.reshape((-1, *windows_labels.shape[-3:]))
    binary_labels = np.any(windows_labels, axis=(1, 2, 3))

    for i, (window_image, window_label, binary_label) in enumerate(
        zip(windows_images, windows_labels, binary_labels)
    ):
        # Including the uid in the filename is really important, otherwise processes
        # will overwrite each other's file. To test if this is happening, just run
        # os.path.isfile(output_path) before writing. If it's true at some point then
        # you got a problem
        # The time() shenanigans are a way to generate a uid, you shouldn't solely rely on it
        # but in combination with the uid and i index, it should be enough
        filename = f"chunk_{uid:07d}_{i:07d}_{int(time()%1*1e9):09d}"
        if binary_label:
            output_path = os.path.join(output_directory, "positive", filename)
            if args.save_masks:
                # If negative, the mask is just zeros so no point storing zeros
                np.savez_compressed(output_path + "_mask.jpg", window_label)
        else:
            output_path = os.path.join(output_directory, "negative", filename)
        imsave(output_path + ".jpg", window_image, check_contrast=False)
        if args.verbose:
            print(output_path, end="\r")
    print(f"Group {uid:05d} done", end="\n" if args.verbose else "\r")
