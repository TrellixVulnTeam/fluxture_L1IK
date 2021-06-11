import argparse
import logging
from typing import Union
import sys

from .fluxture import add_command_subparsers


def get_root_logger() -> logging.Logger:
    l = logging.getLogger(__name__)
    while l.parent:
        l = l.parent
    return l


def setLevel(level: Union[int, str]):
    get_root_logger().setLevel(level)


def main():
    parser = argparse.ArgumentParser(description="Fluxture: a peer-to-peer network crawler")
    parser.add_argument("--debug", action="store_true", help="set the log level to debug")

    add_command_subparsers(parser)

    try:
        args = parser.parse_args()
    except argparse.ArgumentTypeError as e:
        sys.stderr.write(str(e))
        return 1

    if args.debug:
        setLevel(logging.DEBUG)
    else:
        setLevel(logging.INFO)

    return args.func(args)


if __name__ == "__main__":
    main()
