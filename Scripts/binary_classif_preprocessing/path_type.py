from typing import Callable, Union
from argparse import ArgumentTypeError as ArgumentError
import os


class PathType:
    def __init__(
        self,
        exists=True,
        val_type: Union[Callable[[str], bool], str, None] = "file",
        dash_ok=True,
    ):
        """Represent an argument of type path to a file, directory or symlink
        :param exists:
            True: a path that does exist
            False: a path that does not exist, in a valid parent directory
            None: don't care
        :param val_type: file, dir, symlink, None, or a function returning True for valid paths
            None: don't care
        :param dash_ok: whether to allow "-" as stdin/stdout"""

        assert exists in (True, False, None)
        assert val_type in ("file", "dir", "symlink", None) or callable(val_type)

        self._exists = exists
        self._val_type = val_type
        self._dash_ok = dash_ok

    def __call__(self, value):
        if value == "-":
            # the special argument "-" means sys.std{in,out}
            if self._val_type == "dir":
                raise ArgumentError(
                    "standard input/output (-) not allowed as directory path"
                )
            elif self._val_type == "symlink":
                raise ArgumentError(
                    "standard input/output (-) not allowed as symlink path"
                )
            elif not self._dash_ok:
                raise ArgumentError("standard input/output (-) not allowed")
        else:
            file_exists = os.path.exists(value)
            if self._exists:
                if not file_exists:
                    raise ArgumentError("path does not exist: '%s'" % value)
                if self._val_type is None:
                    pass
                elif self._val_type == "file":
                    if not os.path.isfile(value):
                        raise ArgumentError("path is not a file: '%s'" % value)
                elif self._val_type == "symlink":
                    if not os.path.islink(value):
                        raise ArgumentError("path is not a symlink: '%s'" % value)
                elif self._val_type == "dir":
                    if not os.path.isdir(value):
                        raise ArgumentError("path is not a directory: '%s'" % value)
                elif not self._val_type(value):
                    raise ArgumentError("path not valid: '%s'" % value)
            else:
                # Necessary to check if it is False, because None might also eval to False
                if self._exists is False and file_exists:
                    raise ArgumentError("path exists: '%s'" % value)

                parent_dir = os.path.dirname(os.path.normpath(value)) or "."
                if not os.path.isdir(parent_dir):
                    raise ArgumentError(
                        "parent path is not a directory: '%s'" % parent_dir
                    )
                elif not os.path.exists(parent_dir):
                    raise ArgumentError(
                        "parent directory does not exist: '%s'" % parent_dir
                    )

        return value
