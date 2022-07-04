import argparse
import logging
from pathlib import Path

from logger import LOGGING_LEVEL_LIST, ConfigureLogger


def main(file: Path) -> None:
    logger.info("Script start")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A description")

    parser.add_argument(
        metavar="FILES",
        dest="path",
        type=Path,
        nargs="?",
        help="path to the file",
    )
    # ~~~~~~~~~~~~~~~~~ SCRIPT'S SETTINGS ~~~~~~~~~~~~~~~~~#
    settings = parser.add_argument_group(
        "Settings",
        description="",
    )
    settings.add_argument(
        "--log",
        type=str.upper,
        help='choose logging level (default is "INFO")',
        choices=LOGGING_LEVEL_LIST,
        default="INFO",
    )

    args = parser.parse_args()

    # Create logger at the correct level
    ConfigureLogger(log_file="script", console_level=args.log)
    logger = logging.getLogger("log")

    if not args.path:
        parser.error("Just write something.")
    file = args.path.resolve()

    logger.debug(file)

    main(file=file)
