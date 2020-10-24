import argparse
from path_type import PathType


def parse_args():
    main_arg_parser = argparse.ArgumentParser(
        description="Converts multiple JPEG image to chunks and put the chunks into "
        'a "positive" folder if it features a scratch and '
        'a "negative" folder if it does not feature a scratch. '
        "When worker processes go into 'D' status in top/htop, it means they're writing "
        "the images to the disk (uninterruptible sleep). When they're in 'R' status, it means "
        "that they're running the computation (polygons and windows). Watch out the amount of "
        "memory used ! If it hits close to the machine capabilities, workers will be oom killed "
        "without warning and the master process will hang waiting forever ! If this happens, "
        "reduce the group size until it doesn't."
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
        "--overlap",
        default=200,
        metavar="200",
        type=int,
        required=False,
        help="Proportion of pixels in a window that's going to be in common with another window. "
        "Half of the window size is about right. "
        "Default: 200 pixels",
    )

    main_arg_parser.add_argument(
        "-g",
        "--group-size",
        default=30,
        metavar="30",
        type=int,
        required=False,
        help="Number of images to be processed by a single process, if this is set to a value too big,"
        "it might saturate the memory. An efficient solution to avoid memory overflow is to decrease that value."
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
        "-m",
        "--save-masks",
        action="store_true",
        help="Whether to save scratches masks or not. Might be useful one day if we want to predict exact location."
             "Default: don't save masks.",
    )

    main_arg_parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Displays helpful information along",
    )

    return main_arg_parser.parse_args()
