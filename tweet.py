from __future__ import annotations

from typing import TYPE_CHECKING

from api.client import Client
from utils.common import MAX_POST_LENGTH

if TYPE_CHECKING:
    from api.quotes import Quote




client = Client()


def is_text_too_long(text: str) -> bool:
    if len(text) > MAX_POST_LENGTH:
        return True
    return False


def get_post_text(quote: Quote) -> str:
    return (
        f"\"{quote.text}\"\n\n"
        f"— {quote.author}\n\n"
        f"#{quote.category} #wisdom #wordsofwisdom #motivation #mindset"
    )


def run():
    try:
        quote = client.quotes.get_random_quote()
        text = get_post_text(quote)

        while is_text_too_long(text):
            quote = client.quotes.get_random_quote()
            text = get_post_text(quote)

        # client.twitter.create_tweet(text=text)
        # print("Tweet created")

    except Exception as e:
        # TODO: Send email + log
        print(f"Error {e.__class__.__name__}: {e}")
        pass


