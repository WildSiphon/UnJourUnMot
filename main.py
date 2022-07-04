import argparse
import logging

from logger import LOGGING_LEVEL_LIST, ConfigureLogger
from twitter.errors import TwitterConnectionError, TwitterTokenError
from twitter.twitter_bot import BotTwitter


def main() -> None:
    logger.info("Script start")

    twitter_bot = BotTwitter()
    try:
        twitter_bot.run()
    except (TwitterTokenError, TwitterConnectionError, KeyboardInterrupt) as error:
        logger.error(error)
    finally:
        logger.info("Bot stopped")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A description")

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
    ConfigureLogger(console_level=args.log)
    logger = logging.getLogger("log")

    main()
