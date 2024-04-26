"""
Author: Rayla Kurosaki

GitHub: https://github.com/rkp1503
"""
import sys

import requests
from bs4 import BeautifulSoup

from comicinfo import ComicInfo
from src import utils
from src.publishers import seven_seas, square_enix, viz, yen_press


def baka_updates_manga(url: str | None, metadata: ComicInfo) -> None:
    if url is not None:
        author_artist: dict = {"Author(s)": [], "Artist(s)": []}
        genre_b: bool = False
        author_b: bool = False
        artist_b: bool = False
        response: requests.api = requests.get(url)
        soup_1 = BeautifulSoup(response.content, "html.parser")
        for (i, res_cat) in enumerate(soup_1.find_all(class_="sCat")):
            category: str = res_cat.get_text(strip=True)
            if category in ["Genre", "Author(s)", "Artist(s)"]:
                res_content = soup_1.find_all(class_="sContent")
                soup_2 = BeautifulSoup(res_content[i].prettify(),
                                       "html.parser")
                data = soup_2.get_text(strip=True, separator="|").split("|")
                # print(f"\t{data}")
                if category == "Genre":
                    genre_b = True
                    for genre in data[: -1]:
                        metadata.add_genre_or_tag_helper(genre)
                        pass
                    pass
                else:
                    for person in data:
                        if person in utils.PERSON_NAME_CONVERSION.keys():
                            person = utils.PERSON_NAME_CONVERSION[person]
                            pass
                        person = utils.convert_name(person, True)
                        if person not in author_artist[category]:
                            author_artist[category].append(person)
                            pass
                        pass
                    if category == "Author(s)":
                        author_b = True
                        pass
                    else:
                        artist_b = True
                        pass
                    pass
                pass
            if genre_b and author_b and artist_b:
                break
                pass
            pass
        lst_authors: list = author_artist["Author(s)"]
        if len(lst_authors) > 1:
            print(f"\t\tMultiple authors found: {lst_authors}")
            pass
        elif len(lst_authors) == 0:
            print(soup_1.prettify())
            sys.exit("\tNo authors found")
            pass
        metadata.set_authors(lst_authors)
        lst_artists: list = author_artist["Artist(s)"]
        if len(lst_artists) > 1:
            print(f"\t\tMultiple authors found: {lst_authors}")
            pass
        elif len(lst_artists) == 0:
            print(soup_1.prettify())
            sys.exit("\tNo artists found")
            pass
        metadata.set_artists(lst_artists)
        pass
    return None


def my_anime_list(url: str | None, metadata: ComicInfo) -> None:
    if url is not None:
        response: requests.api = requests.get(url)
        soup_1 = BeautifulSoup(response.content, "html.parser")
        results = soup_1.find(class_="leftside")
        for res_1 in results.find_all(class_="spaceit_pad"):
            result = res_1.find("span", class_="dark_text")
            category: str = result.get_text(strip=True)
            if category == "Japanese:":
                data: str = res_1.get_text(strip=True).split(":")[-1]
                metadata.set_japanese_title(data)
                pass
            elif category in ["Genres:", "Theme:", "Demographic:", ]:
                soup_2 = BeautifulSoup(res_1.prettify(), "html.parser")
                for res_2 in soup_2.find_all(itemprop="genre"):
                    genre: str = res_2.get_text(strip=True)
                    metadata.add_genre_or_tag_helper(genre)
                    pass
                pass
            pass
        pass
    return None


def web_scraper_wiki(url: str | None, metadata: ComicInfo) -> None:
    if url is not None:
        manga_b: bool = False
        genre_b: bool = False
        demographic_b: bool = False
        response: requests.api = requests.get(url)
        soup_1 = BeautifulSoup(response.content, "html.parser")
        table = soup_1.find("table", class_="infobox")
        for (i, res_tr) in enumerate(table.find_all("tr")):
            soup_2 = BeautifulSoup(res_tr.prettify(), "html.parser")
            res_th = soup_2.find("th", class_="infobox-label")
            if (res_th is not None) and manga_b:
                category: str = res_th.get_text(strip=True)
                if category in ["Genre", "Demographic"]:
                    for res_a in soup_2.find("td").find_all("a"):
                        if res_a.has_attr("title"):
                            genre_tag: str = res_a.get_text(strip=True).title()
                            metadata.add_genre_or_tag(genre_tag)
                            if category == "Genre":
                                genre_b = True
                                pass
                            else:
                                demographic_b = True
                                pass
                            pass
                        pass
                    pass
                pass
            else:
                field: str = "infobox-subheader"
                res_td = soup_2.find("td", colspan="2", class_=field)
                if res_td is not None:
                    sub_header: str = res_td.get_text(strip=True)
                    manga_b = (sub_header == "Manga") or (i == 0)
                    pass
                pass
            if manga_b and genre_b and demographic_b:
                break
                pass
            pass
        pass
    return None


def web_scraper_publisher(url: str, metadata: ComicInfo) -> None:
    src: str = url.split("/")[2]
    if " " in src:
        pass
    elif "xxx" in src:
        metadata.set_publisher("Denpa")
        # web_scraper_xxx(url, metadata)
        pass
    elif "xxx" in src:
        metadata.set_publisher("Futabasha")
        # web_scraper_xxx(url, metadata)
        pass
    elif "xxx" in src:
        metadata.set_publisher("J-Novel Club")
        # web_scraper_xxx(url, metadata)
        pass
    elif "kodansha" in src:
        metadata.set_publisher("Kodansha USA")
        # web_scraper_kodansha(url, metadata)
        pass
    elif "sevenseasentertainment" in src:
        metadata.set_publisher("Seven Seas Entertainment")
        seven_seas.web_scraper(url, metadata)
        pass
    elif "squareenixmangaandbooks" in src:
        metadata.set_publisher("Square Enix USA")
        square_enix.web_scraper(url, metadata)
        pass
    elif "viz" in src:
        metadata.set_publisher("Viz")
        viz.web_scraper(url, metadata)
        pass
    elif "yenpress" in src:
        metadata.set_publisher("Yen Press")
        yen_press.web_scraper(url, metadata)
        pass
    return None
