import os
from dotenv import load_dotenv

import tweepy

from . import quotes


load_dotenv()

TWITTER_ACCESS_KEY = os.getenv("TWITTER_ACCESS_KEY")
TWITTER_ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
QUOTES_API_KEY = os.getenv("QUOTES_API_KEY")


class Client:
    def __init__(self):
        auth = tweepy.OAuth1UserHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
        auth.set_access_token(TWITTER_ACCESS_KEY, TWITTER_ACCESS_SECRET)

        self.twitter_v1 = tweepy.API(auth)
        self.twitter_v2 = tweepy.Client(
            access_token=TWITTER_ACCESS_KEY,
            access_token_secret=TWITTER_ACCESS_SECRET,
            consumer_key=TWITTER_API_KEY,
            consumer_secret=TWITTER_API_SECRET,
        )
        self.quotes = quotes.Client(token=QUOTES_API_KEY)
