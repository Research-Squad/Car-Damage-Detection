import numpy as np
from skimage.util.shape import view_as_windows


def windowify(args, masked_image_array: np.ndarray) -> np.ndarray:
    """
    Creates chunks (or windows) from the given array using the window size/overlap from args
    :param args: arguments from the arg parser
    :param masked_image_array: a numpy array of shape (BATCH, WIDTH, HEIGHT, CHANNELS)
    :return: a numpy view of the array with shape (BATCH, CHUNK_X, CHUNK_Y, WINDOW_SIZE, WINDOW_SIZE, CHANNELS)
    """
    shape_windows = (1, args.window_size, args.window_size, masked_image_array.shape[-1])
    step = (
        1,
        find_step(masked_image_array.shape[-2], shape_windows[0], args.overlap),
        find_step(masked_image_array.shape[-3], shape_windows[1], args.overlap),
        1,
    )
    windows = view_as_windows(masked_image_array, window_shape=shape_windows, step=step)
    windows = np.squeeze(windows)  # Removes unitary dimensions caused by step 1 in the last dimension
    return windows


def find_step(height: int, window_size: int, overlap: int) -> int:
    """
    height: image's height, or width or whatever size you want to put the overlapping windows into
    window_size: the size of the windows, every window has the same size
    overlap: the size of the overlap between two windows

    You should have overlap < window_size < height !

    For the formulae detailed, see notebook "Windowify.ipynb"@2020-09-06
    """
    assert overlap < window_size, "Windows can't overlap more than twice !"
    assert window_size < height, "Window size must be smaller than height !"
    return int(height * (window_size - overlap) / (height + window_size))

