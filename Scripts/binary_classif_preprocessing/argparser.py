import argparse
from path_type import PathType


def parse_args():
    main_arg_parser = argparse.ArgumentParser(
        description="Converts multiple JPEG image to chunks and put the chunks into "
        'a "positive" folder if it features a scratch '
        'a "negative" folder if it does not feature a scratch'
    )

    main_arg_parser.add_argument(
        "-i",
        "--input",
        metavar="/path/to/datasetFolder",
        type=PathType(exists=True, val_type="dir"),
        required=True,
        help="Path to the dataset folder, for any JPEG image in it, it needs "
        "to contain a corresponding JSON file in LabelMe format.",
    )

    main_arg_parser.add_argument(
        "-o",
        "--output",
        metavar="/path/to/outputDir",
        type=PathType(exists=None, val_type="dir"),
        required=True,
        help="Output directory in which will be put the labelled chunks. "
        "Will contain a `positive` subdir and a `negative` subdir, "
        "with chunks going into either of them based on their label. "
        "This directory doesn't need to exists before "
        "running this program.",
    )

    main_arg_parser.add_argument(
        "--window-size",
        default=500,
        metavar="500",
        type=int,
        required=False,
        help="Size of the square window to use, i.e. their height/width in pixels. "
        "Default: 500 pixels",
    )

    main_arg_parser.add_argument(
        "-g",
        "--group-size",
        default=30,
        metavar="30",
        type=int,
        required=False,
        help="Number of images to be processed by a single process, if this is set to a value too big,"
        "it might saturate the memory. "
        "Default: 500 pixels",
    )

    main_arg_parser.add_argument(
        "-j",
        "--jobs",
        default=None,
        metavar="$(nproc)-1",
        type=int,
        required=False,
        help="Number of processes to run in parallel, should not exceed the core count (see man nproc)."
        "Default: $(nproc) - 1",
    )

    main_arg_parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Displays helpful information along",
    )

    return main_arg_parser.parse_args()
