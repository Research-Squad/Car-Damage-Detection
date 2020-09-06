from typing import List, Tuple
from os import PathLike
import json
import numpy as np
from skimage.io import imread
from skimage.draw import polygon2mask


def load_images(filenames: List[PathLike]) -> np.ndarray:
    """
    Loads
    :param filenames:
    :return:
    """
    images = []
    for filename in filenames:
        images.append(imread(filename))

    return np.array(images)


def load_masks(filenames: List[PathLike], image_shape: Tuple[int, int] = None) -> np.ndarray:
    """
    Loads multiple polygons coordinates from many JSON files and converts them into boolean masks
    :param filenames: JSON files containing LabelMe data.
    :param image_shape: The size of the image to mask. If None is provided (default), the image size specified in the
     labels will be used. It is assumed all the labels refer to images of the same size of course.
    :return: a numpy array of dtype boolean and of shape [numberOfLabelFiles, image_shape[0], image_shape[1]]
     where True means that it's inside a labeled polygon, and False means it's outside.
    """
    json_labels = []
    for filename in filenames:
        with open(filename, 'r') as f:
            json_labels.append(json.load(f))

    # Contains each label's boolean mask
    labels_masks = []
    for json_label in json_labels:
        if image_shape is None:
            image_shape = json_label['imageWidth'], json_label['imageHeight']
        # Overlaps all the label's polygons onto a single boolean mask
        label_mask = np.zeros(image_shape, dtype=np.bool)
        for shape in json_label['shapes']:
            if shape['shape_type'] != 'polygon':
                continue
            mask = polygon2mask(image_shape, shape['points'])
            label_mask |= mask
        labels_masks.append(label_mask)

    return np.asarray(labels_masks)
