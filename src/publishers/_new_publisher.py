"""
Author: Rayla Kurosaki

GitHub: https://github.com/rkp1503
"""

import sys

import requests
from bs4 import BeautifulSoup

from src.comicinfo import ComicInfo

AGE_RATINGS: dict = {
    "": 18,
    "": 17,
    "": 15,
    "": 13,
    "": 10,
    "": 8,
    "": 6,
    "": 3,
    "": 0,
}


def web_scraper(url: str, metadata: ComicInfo) -> None:
    response: requests.api = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        pass
    else:
        sys.exit(f"\t\t\tStatus code: {response.status_code}. "
                 f"Failed to fetch URL: {url}.")
        pass
    return None
