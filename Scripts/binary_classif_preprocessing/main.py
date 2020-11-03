#!/usr/bin/env python3
"""
    Converts multiple JPEG image to chunks and put the chunks into 
    a "positive" folder if it features a scratch
    a "negative" folder if it does not feature a scratch
"""

import os
import argparse
from pathlib import Path
from multiprocessing import Pool, cpu_count
from argparser import parse_args
from load_data import check_matching_json_jpeg, group_paths, load_label_dict
from process_files import worker


def main():
    """Main function"""
    args = parse_args()
    if not check_matching_json_jpeg(args.input):
        print(f"Found lone json/jpeg files under {args.input}")
        exit(1)

    make_output_dirs(args)

    label_dict = load_label_dict(Path("label_dictionary.json"))
    accepted_labels = (
        label_dict["bump"]
        .union(label_dict["corrosion"])
        .union(label_dict["scratch"])
        .union(label_dict["crack"])
        .union(label_dict["dirt"])
        .union(label_dict["rim_damage"])
    )

    images_groups = group_paths(args.input, group_size=args.group_size)
    print(f"Running {len(images_groups)} groups, each of {args.group_size} images")
    map_arg = zip(
        [args] * len(images_groups),
        [accepted_labels] * len(images_groups),
        list(range(len(images_groups))),
        images_groups,
    )

    with Pool(processes=args.jobs if args.jobs is not None else (cpu_count() - 1)) as p:
        _ = p.starmap(func=worker, iterable=map_arg)

    print("Alles gut товарищи !")


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
