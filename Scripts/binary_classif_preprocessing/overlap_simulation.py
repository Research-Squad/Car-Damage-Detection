#!/usr/bin/env python3
"""Computes the processed data size and various stats"""


def main():
    """Main function"""
    im_width, window_width, overlap_width = 4096, 500, 200
    im_height, window_height, overlap_height = 3000, 300, 200

    w_size = [window_height, window_width]
    im_shape = [im_height, im_width]
    overlap = [overlap_height, overlap_width]
    for name, i in zip(["Height", "Width"], range(2)):
        print(name, "statistics")
        # w: window size
        # o: overlap size
        # h: height (or width when dealing with width, but let's pretend we're dealing w/ height)
        w, o, h = w_size[i], overlap[i], im_shape[i]
        step = w - o
        # Proved by testing, like a true engineer
        number_of_windows = (h - w) // step + 1
        # At the far right, when we can't put any more window, we're losing pixels
        lost_border = h - (h // step * step)
        # If we concatenated all the windows together
        output_size = number_of_windows * w

        print(f"\tLosing \t\t\t\t{lost_border} px ~ {lost_border/h:.2%}")
        print(f"\tOutput size of \t\t{output_size} px")
        print(f"\tIncreased input by \t{output_size-h}px ~ {output_size/h-1:.2%}")


if __name__ == "__main__":
    main()
