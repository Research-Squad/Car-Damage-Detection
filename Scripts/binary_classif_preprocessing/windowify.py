import numpy as np
from skimage.util.shape import view_as_windows


def windowify(
    masked_image_array: np.ndarray, window_size: int, overlap: int
) -> np.ndarray:
    """
    Creates chunks (or windows) from the given array using the window size/overlap from args
    :param masked_image_array: a numpy array of shape (BATCH, WIDTH, HEIGHT, CHANNELS)
    :param window_size: window size to use, in pixels
    :param overlap: proportion of pixels in a window that's going to be in common with another window
    :return: a numpy view of the array with shape (BATCH, CHUNK_X, CHUNK_Y, WINDOW_SIZE, WINDOW_SIZE, CHANNELS)
    """
    shape_windows = (1, window_size, window_size, masked_image_array.shape[-1])
    step = (
        1,  # Batch dimension
        window_size - overlap,
        window_size - overlap,
        1,  # Colour channels
    )
    windows = view_as_windows(masked_image_array, window_shape=shape_windows, step=step)
    # Removes unitary dimensions caused by step 1 in the last dimension
    windows = np.squeeze(windows)
    return windows
