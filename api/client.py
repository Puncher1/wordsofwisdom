import os
from dotenv import load_dotenv

import tweepy

from . import quotes


load_dotenv()

TWITTER_ACCESS_KEY = os.getenv("TWITTER_ACCESS_KEY")
TWITTER_ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")
TWITTER_CONSUMER_KEY = os.getenv("TWITTER_CONSUMER_KEY")
TWITTER_CONSUMER_SECRET = os.getenv("TWITTER_CONSUMER_SECRET")
QUOTES_API_KEY = os.getenv("QUOTES_API_KEY")


class Client:
    def __init__(self):
        self.twitter = tweepy.Client(
            access_token=TWITTER_ACCESS_KEY,
            access_token_secret=TWITTER_ACCESS_SECRET,
            consumer_key=TWITTER_CONSUMER_KEY,
            consumer_secret=TWITTER_CONSUMER_SECRET,
        )
        self.quotes = quotes.Client(token=QUOTES_API_KEY)
