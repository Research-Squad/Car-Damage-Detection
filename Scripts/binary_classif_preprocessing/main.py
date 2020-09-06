#!/usr/bin/env python3
"""
    Converts multiple JPEG image to chunks and put the chunks into 
    a "positive" folder if it features a scratch
    a "negative" folder if it does not feature a scratch
"""

import os
from os import PathLike
import argparse
import numpy as np
from argparser import parse_args


def main():
    """Main function"""
    args = parse_args()
    make_output_dirs(args)
    print(args.window_size, args.overlap)


def make_output_dirs(args: argparse.ArgumentParser) -> None:
    """
    Creates args.output/positive and args.output/negative directories.
    Doesn't throw an error if they exists.
    Defines args.positive and args.negative with path to their respective directories.
    :param args: the argument parser's returned object
    :return: None
    """
    assert hasattr(args, "output"), "Output not specified in arguments object"
    args.positive = os.path.join(args.output, "positive")
    args.negative = os.path.join(args.output, "negative")
    os.makedirs(args.positive, exist_ok=True)
    os.makedirs(args.negative, exist_ok=True)


if __name__ == "__main__":
    main()
