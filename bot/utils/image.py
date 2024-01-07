from __future__ import annotations

import os
import textwrap
from typing import TYPE_CHECKING

from PIL import Image, ImageDraw, ImageFont

if TYPE_CHECKING:
    from ..api.quotes import Quote


QUOTE_FONT = "./bot/resources/Roboto-Regular.ttf"
AUTHOR_FONT = "./bot/resources/Roboto-LightItalic.ttf"
CATEGORY_FONT = "./bot/resources/Roboto-Light.ttf"
IMG_OUTPUT_PATH = "./bot/resources/post_img.png"

bg_img = Image.open("./bot/resources/Post_Background.png")


def create_quote_image(quote: Quote) -> str:
    quote_font = ImageFont.truetype(QUOTE_FONT, 28)
    author_font = ImageFont.truetype(AUTHOR_FONT, 20)
    category_font = ImageFont.truetype(CATEGORY_FONT, 14)

    quote_text = quote.text
    author_text = quote.author
    category_text = quote.category.capitalize()

    quote_draw = ImageDraw.Draw(bg_img)
    x = 255
    quote_y = 160
    for line in textwrap.wrap(quote_text, width=47):
        quote_draw.text((x, quote_y), line, fill="#ffffff", font=quote_font)
        quote_y += quote_font.getsize(line)[1] + 10

    author_draw = ImageDraw.Draw(bg_img)
    author_draw.text((x, 400), author_text, fill="#ffffff", font=author_font)

    category_draw = ImageDraw.Draw(bg_img)
    _, _, w, h = category_draw.textbbox((0, 0), category_text, font=category_font)
    category_draw.text(((1024-w)/2, 115), category_text, font=category_font, fill="#a0a0a0")

    img_w, img_h = bg_img.size
    bg_img.crop((100, 0, img_w-100, img_h)).save(IMG_OUTPUT_PATH, quality=10)

    return IMG_OUTPUT_PATH
