from __future__ import annotations

from typing import TYPE_CHECKING

import mail_support
from .api.client import Client
from .utils.common import MAX_POST_LENGTH
from .image import create_quote_image

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

        img_out_path = create_quote_image(quote)
        media_img = client.twitter_v1.media_upload(filename=img_out_path)
        media_img_id = media_img.media_id  # type: ignore # is not None

        client.twitter_v2.create_tweet(text=text, media_ids=[media_img_id])
        print("Tweet created")

    except Exception as e:
        # TODO: Send email + log
        raise e
