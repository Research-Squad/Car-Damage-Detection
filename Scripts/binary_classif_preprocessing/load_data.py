from typing import List, Tuple, Set, Dict
from os import PathLike
import os
from pathlib import Path
import json
import numpy as np
from skimage.io import imread
from polygon2mask import polygon2mask


def group_paths(directory: PathLike, group_size: int) -> List[List[PathLike]]:
    images: List[Path] = [
        Path(os.path.join(directory, f))
        for f in os.listdir(directory)
        if f.endswith(".jpg")
    ]
    images_groups: List[List[Path]] = [
        images[i : i + group_size] for i in range(0, len(images), group_size)
    ]
    return images_groups


def load_images(filenames: List[PathLike]) -> np.ndarray:
    """
    Loads images into a numpy array
    :param filenames: JPEG files to load
    :return: a numpy array of shape [numberOfImageFiles, image_shape[0], image_shape[1], image_shape[2]]
    """
    images = []
    for filename in filenames:
        images.append(imread(str(filename)))

    return np.array(images)


def load_label_dict(filename: PathLike) -> Dict[str, Set[str]]:
    with open(filename, "r") as f:
        raw_label_dict: Dict[str, List[str]] = json.load(f)

    label_dict: Dict[str, Set[str]] = {k: set(v) for k, v in raw_label_dict.items()}
    for k in label_dict.keys():
        if k not in label_dict[k]:
            label_dict[k].add(k)

    return label_dict


def load_masks(
    filenames: List[PathLike],
    accepted_labels: Set[str],
    image_shape: Tuple[int, int] = None,
) -> np.ndarray:
    """
    Loads multiple polygons coordinates from many JSON files and converts them into boolean masks
    :param filenames: JSON files containing LabelMe data.
    :param accepted_labels: A set of all the labels that should be integrated into the masks
    :param image_shape: The size of the image to mask. If None is provided (default), the image size specified in the
     labels will be used. It is assumed all the labels refer to images of the same size of course.
    :return: a numpy array of dtype boolean and of shape [numberOfLabelFiles, image_shape[0], image_shape[1]]
     where True means that it's inside a labeled polygon, and False means it's outside.
    """
    json_labels = []
    for filename in filenames:
        with open(filename, "r") as f:
            json_labels.append(json.load(f))

    # Contains each label's boolean mask
    labels_masks = []
    for json_label in json_labels:
        if image_shape is None:
            # Beware that some json might have these set to 0,0
            image_shape = json_label["imageWidth"], json_label["imageHeight"]
        # Overlaps all the label's polygons onto a single boolean mask
        label_mask = np.zeros(image_shape, dtype=np.bool)
        for shape in json_label["shapes"]:
            if shape["shape_type"] != "polygon":
                continue
            if shape["label"] not in accepted_labels:
                continue

            # Points coordinates were actually the wrong way around,
            # it was really hard to spot...
            points = []
            for entry in shape["points"]:
                # Yes, having a json null coordinate happened in the past
                if entry[0] is not None and entry[1] is not None:
                    points.append([entry[1], entry[0]])

            if len(points) != 0:
                mask = polygon2mask(image_shape, points)
                label_mask |= mask

        labels_masks.append(label_mask)

    return np.asarray(labels_masks)


def check_matching_json_jpeg(directory: PathLike) -> bool:
    """
    Checks that the provided directory contains only pairs of JPEG and JSON files,
    and no lone JPEG or lone JSON file.
    Ignores any file that doesn't end in .jpg or .json
    :param directory: Directory which to check the content of
    :returns: True if all JPEG files got an associated JSON file and all JSON files got an associated JPEG file.
    """
    files = [f for f in os.listdir(directory) if f.endswith((".jpg", ".json"))]
    #if (
    #    len(files) & 1
    #):  # We should have an even number of files since they come in pairs
    #    return False
    for f in files:
        if f.endswith(".json") and f.replace(".json", ".jpg") not in files:
            print(f)
            return False
        if f.endswith(".jpg") and f.replace(".jpg", ".json") not in files:
            print(f)
            return False
    return True
