# Command line interface.
import sys, os
import argparse, traceback

import logging
from .logger import logger, set_logging_level

log = logger(__name__)

description = "Artifex is a pysible project builder"
epilog = """\
        You probably want "artifex init <project name> -i" \n\n
    """


class ArtifexError(Exception):
    pass


def as_options(parser):
    action = parser.add_subparsers(dest="action")

    # Create a new SPORK
    init_action = action.add_parser("init", help="Create files for a  new board")
    init_action.add_argument(
        "ProjectName",
        default="MyThing",
        help="Specify the name of the class to generate",
    )
    init_action.add_argument(
        "-c", "--construct", help="Select a construct", default=None
    )
    init_action.add_argument(
        "-f", "--force", help="Force creation", action="store_true"
    )
    init_action.add_argument(
        "-i", "--interactive", help="Interactive creation", action="store_true"
    )
    init_action.add_argument(
        "--local",
        help="Create local files, does not need to run",
        action="store_true",
    )

    # Create a new thingo
    action.add_parser("new", help="Create a new dirver,peripheral,construct,core ")

    # List boards and active peripherals
    action.add_parser("list", help="List available projects")

    # Developer tools

    return parser


def as_main(args=None):
    if args is None:
        parser = argparse.ArgumentParser(description=description, epilog=epilog)
        parser.add_argument("-v", help="Warn Logging Level", action="store_true")
        parser.add_argument("-vv", help="Info Logging Level", action="store_true")
        parser.add_argument("-vvv", help="Debug Logging Level", action="store_true")
        # Unfinished
        parser.add_argument(
            "-d", "--directory", help="Directory for spork file", default="."
        )
        args = as_options(parser).parse_args()

    # Turn on verbosity
    if args.v:
        set_logging_level(logging.WARNING)
    if args.vv:
        set_logging_level(logging.INFO)
    if args.vvv:
        set_logging_level(logging.DEBUG)

    # Check for the .spork file
    the_spork = None
    try:
        # TODO use directory for this file
        s = os.stat(".artifex")
        log.debug("spork file exists")
        the_spork = load_spork(".artifex")
    except FileNotFoundError:
        log.error("{:s}".format(str(traceback.print_exc())))
        log.critical(".artifex file missing")
        log.critical("Please template the .artifex file")
        print("No .artifex file")


    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    if args.action == "init":
        if len(sys.argv) == 2:
            log.critical("Define a New Project")
        log.critical(args.ProjectName)

    if args.action == "new":
        log.error("New is (UNFINISHED)")

    if args.action == "info":
        log.critical(".artifex file does not exist")
        raise ArtifexError("Spork info UNFINISHED")

    if args.action == "console":
        from .host.console import Console

        console = Console()
        console.attach()
        console.command_line()

    if args.action == "status":
        raise SporkError("UNFINISHED  - Status not working yet, get board status")

    if args.action == "update":
        raise SporkError("UNFINISHED  - Update not working yet, get board status")

    if args.action == "list":
        from .templates.short_list import short_list

        print(" Available Projects")
        print()
        for num, board in enumerate(short_list()):
            print("{:>4}  {}".format(num, board))
        print()

    if args.action == "build":
        log.error("build is (UNFINISHED)")
        raise SporkError("UNFINISHED - Build unfinished: make physible")
