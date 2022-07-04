import logging

from twitter.tweepy_wrapper import TweepyWrapper

logger = logging.getLogger("log")


class BotTwitter:
    """
    The Twitter Bot.
    """

    def __init__(self):
        """
        Construct the bot.

        :raise TwitterTokenError:
        """
        # Tweepy configuration
        self.tweepy_wrapper = TweepyWrapper()

    def run(self) -> None:
        """
        Brings bot to life.

        :raise TwitterConnectionError:
        """
        self.tweepy_wrapper.connect()
        logger.info(f"Connected to '{self.name}' @{self.screen_name}\n")

        self.post("This is fine")

    def post(self, msg: str = "Test but no text") -> None:
        self.tweepy_wrapper.post(msg=msg)

    @property
    def name(self):
        return self.tweepy_wrapper.name

    @property
    def screen_name(self):
        return self.tweepy_wrapper.screen_name
