import json
import random
import requests
from typing import TypedDict, List

from utils.common import CATEGORIES, TEXT_LENGTH


class QuotePayload(TypedDict):
    quote: str
    author: str
    category: str


class Quote:
    def __init__(self, *, data: QuotePayload):
        self.text = data["quote"]
        self.author = data["author"]
        self.category = data["category"]

    def __repr__(self):
        return f"<Quote author={self.author} text={self.text} category={self.category}>"


class Client:
    API_URL = "https://api.api-ninjas.com/v1/quotes?category={}"

    def __init__(self, token: str):
        self.token = token

    def _fetch_quote(self, category: str) -> List[QuotePayload]:
        headers = {"X-Api-Key": self.token}
        response = requests.get(self.API_URL.format(category), headers=headers)

        if response.status_code == requests.codes.ok:
            return response.json()
        else:
            print("Error:", response.status_code, response.text)

    def get_random_quote(self) -> Quote:
        weight_except_first = [0.07777 for _ in range(len(CATEGORIES) - 1)]
        category = random.choices(CATEGORIES, weights=([0.3] + weight_except_first))[0]

        data = self._fetch_quote(category)[0]
        return Quote(data=data)
