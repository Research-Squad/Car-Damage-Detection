import numpy as np
from skimage.util.shape import view_as_windows


def windowify(masked_image_array: np.ndarray, window_size: int) -> np.ndarray:
    """
    Creates chunks (or windows) from the given array using the window size/overlap from args
    :param masked_image_array: a numpy array of shape (BATCH, WIDTH, HEIGHT, CHANNELS)
    :param window_size: window size to use, in pixels
    :return: a numpy view of the array with shape (BATCH, CHUNK_X, CHUNK_Y, WINDOW_SIZE, WINDOW_SIZE, CHANNELS)
    """
    shape_windows = (1, window_size, window_size, masked_image_array.shape[-1])
    step = (
        1,
        find_step(masked_image_array.shape[1], shape_windows[1]),
        find_step(masked_image_array.shape[2], shape_windows[2]),
        1,
    )
    windows = view_as_windows(masked_image_array, window_shape=shape_windows, step=step)
    windows = np.squeeze(
        windows
    )  # Removes unitary dimensions caused by step 1 in the last dimension
    return windows


def find_step(height: int, window_size: int) -> int:
    """
    :param height: image's height, or width or whatever size you want to put the overlapping windows into
    :param window_size: the size of the windows, every window has the same size

    You should have window_size < height !

    For the formulae detailed, see notebook "Windowify.ipynb"@2020-09-06
    """
    assert window_size < height, "Window size must be smaller than height !"
    n = int(height / window_size) + 1
    overlap = int((window_size * n - height) / (n + 1))
    return window_size - overlap
