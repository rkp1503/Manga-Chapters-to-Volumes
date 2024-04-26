"""
Author: Rayla Kurosaki

GitHub: https://github.com/rkp1503
"""

import utils

TAGS: list = [
    "Josei", "Kids", "Seinen", "Shōjo", "Shōnen",
]

RENAME_GENRES_TAGS: dict = {
    "Shoujo": "Shōjo",
    "Shojo": "Shōjo",
    "Shōjo Ai": "Girls Love",
    "Shoujo Ai": "Girls Love",
    "Shojo Ai": "Girls Love",
    "Yuri": "Girls Love",
    "girls' love": "Girls Love",
    "Shounen": "Shōnen",
    "Shonen": "Shōnen",
    "Shōnen Ai": "Boys Love",
    "Shounen Ai": "Boys Love",
    "Shonen Ai": "Boys Love",
    "Yaoi": "Boys Love",
    "boys' love": "Boys Love",
    "Science Fiction": "Sci-Fi",
    "Science Fiction Comedy": "Sci-Fi Comedy",
    "Gender Bender": "Magical Sex Change",
    "Magical Sex Shift": "Magical Sex Change",
    "School": "School Life",
    "Slice-of-Life": "Slice of Life",
}

IGNORE_GENRES_TAGS: list = [
    # Baka-Updates Manga
    "Adult", "Doujinshi", "Historical", "Mature",
    # My Anime List
    "Avant Garde", "Award Winning", "Gourmet", "Adult Cast", "Anthropomorphic",
    "Childcare", "Educational", "Historical", "Iyashikei", "Medical", "Memoir",
    "Pets",
    # Wikipedia
    # Seven Seas
    "4koma", "Alice in Wonderland", "Autobiography", "Based on a Video Game",
    "Cats", "Classic Novels", "Classics", "Color", "Danmei",
    "Encyclopedia/Guides", "Encyclopedia", "Guides", "English Original",
    "Hatsune Miku", "LGBT+ Topics", "Manhua", "Manhwa", "Novel",
    "Period Piece", "Webcomics",
    # Square Enix
    "Game Tie-In", "Light Novel Tie-In", "Game Tie-In", "LGBTQIA+",
    "Media Tie-in", "Adult / Mature", "Historical Fiction",
    "Original Light Novel",
    # Viz
    "LGBT",
    # Yen Press
    "Anime Tie-in", "LGBTQ", "Light Novel Tie-In", "Special Interest",
    "Video Game Tie-in"
]

SERIES_XDRESSING_MAGICAL_SEX_CHANGE: dict = {
    "Crossdressing": [
        "Aoharu X Machinegun", "If Witch, Then Which?", "So Cute It Hurts!!"
    ],
    "Magical Sex Change": [
        "Pretty Face", "Though You May Burn to Ash", "So Cute It Hurts!!"
    ]
}

SERIES_SPORTS: dict = {
    "Airsoft": [
        "Aoharu X Machinegun",
    ],
    "Basketball": [
        "Kuroko’s Basketball",
    ],
    "Tennis": [
        "The Prince of Tennis",
    ],
    "Volleyball": [
        "Haikyu!!",
    ],
}

GENRES_SPLIT_AND: list = [
    "Action and Adventure", "Crime and Mystery",
]

GENRES_SPLIT_AND_B: list = [
    "Crime & Mystery",
]
GENRES_SPLIT_DASH: list = [
    "Action-Adventure",
]
GENRES_SPLIT_SLASH_A: list = [
    "Action / Adventure", "Mystery / Thriller", "Shojo / Josei"
]
GENRES_SPLIT_SLASH_B: list = [
    "Action/Adventure", "BL/Yaoi", "GL/Yuri",
]

KOMGA_AGE_RATING: dict = {
    18: "Adults Only 18+",
    17: "Mature 17+",
    15: "MA 15+",
    13: "Teen",
    10: "Everyone 10+",
    8: "PG",
    6: "Kids to Adults",
    3: "Early Childhood",
    0: "Everyone",
}


class ComicInfo:
    def __init__(self):
        # Series Data
        self.series: str = ""
        self.japanese_title: str = ""
        self.status: str = ""
        self.count: int = -1
        # self.alternate_series: str = ""
        # self.alternate_number: str = ""
        # self.alternate_count: int = -1
        self.publisher: str = ""
        self.imprint: str = ""
        self.genres: list = []
        self.tags: list = []
        self.language_ISO: str = ""
        self.groups: list = []

        # Book Data
        self.title: str = ""
        self.number: str = ""
        self.volume: str = ""
        # self.alternate_series: str = ""
        # self.alternate_number: str = ""
        # self.alternate_count: int = -1
        self.summary: str = ""
        self.year: int = -1
        self.month: int = -1
        self.day: int = -1
        self.authors: list = []
        self.artists: list = []
        self.inkers: list = []
        self.colorists: list = []
        self.letterers: list = []
        self.cover_artists: list = []
        self.editors: list = []
        self.translators: list = []
        self.urls: list = []
        self.page_count: int = 0
        self.format: str = ""
        self.black_and_white: bool = False
        self.characters: list = []
        self.teams: list = []
        self.locations: list = []
        self.main_character_or_team: str = ""
        self.story_arc: str = ""
        self.story_arc_number: str = ""
        self.age_rating: str = "Unknown"
        self.age_rating_publisher: str = "Unknown"
        self.community_rating: float = -1.0
        self.review: str = ""
        self.isbn: str = ""

        # Other Data
        self.notes: str = ""
        self.scan_information: str = ""
        pass

    def get_series_title(self) -> str:
        return self.series

    def set_series_title(self, series_title: str) -> None:
        self.series = series_title
        return None

    def get_japanese_title(self) -> str:
        return self.japanese_title

    def set_japanese_title(self, japanese_title: str) -> None:
        self.japanese_title = japanese_title
        return None

    def get_status(self) -> str:
        return self.status

    def set_status(self, status: str) -> None:
        self.status = status
        return None

    def get_count(self) -> int:
        return self.count

    def set_count(self, count: int) -> None:
        self.count = count
        return None

    # def get_alternate_series(self) -> str:
    #     return self.alternate_series
    #
    # def set_alternate_series(self, alternate_series: str) -> None:
    #     self.alternate_series = alternate_series
    #     return None
    #
    # def get_alternate_number(self) -> str:
    #     return self.alternate_number
    #
    # def set_alternate_number(self, alternate_number: str) -> None:
    #     self.alternate_number = alternate_number
    #     return None
    #
    # def get_alternate_count(self) -> int:
    #     return self.alternate_count
    #
    # def set_alternate_count(self, alternate_count: int) -> None:
    #     self.alternate_count = alternate_count
    #     return None

    def get_publisher(self) -> str:
        if self.imprint != "":
            if self.imprint != self.publisher:
                return f"{self.publisher} ({self.imprint})"
            else:
                return self.publisher
            pass
        else:
            return self.publisher
        pass

    def set_publisher(self, publisher: str) -> None:
        self.publisher = publisher
        return None

    def get_imprint(self) -> str:
        return self.imprint

    def set_imprint(self, imprint: str) -> None:
        self.imprint = imprint
        return None

    def get_genres(self) -> list:
        return self.genres

    def set_genres(self, genres: list) -> None:
        self.genres = genres
        return None

    def get_tags(self) -> list:
        return self.tags

    def set_tags(self, tags: list) -> None:
        self.tags = tags
        return None

    def add_genre_or_tag(self, e: str) -> None:
        if e not in IGNORE_GENRES_TAGS:
            if e in RENAME_GENRES_TAGS:
                e: str = RENAME_GENRES_TAGS[e]
                pass
            if e in TAGS:
                if e not in self.tags:
                    self.tags.append(e)
                    pass
                pass
            else:
                if e not in self.genres:
                    self.genres.append(e)
                    pass
                pass
            pass
        return None

    def add_genre_or_tag_helper(self, e: str) -> None:
        if e in GENRES_SPLIT_AND:
            self.add_genres_or_tags(e.split(" and "))
            pass
        elif e in GENRES_SPLIT_DASH:
            self.add_genres_or_tags(e.split("-"))
            pass
        elif e in GENRES_SPLIT_SLASH_A:
            self.add_genres_or_tags(e.split(" / "))
            pass
        elif e in GENRES_SPLIT_SLASH_B:
            self.add_genres_or_tags(e.split("/"))
            pass
        else:
            self.add_genre_or_tag(e.strip())
            pass
        return None

    def add_genres_or_tags(self, lst: list) -> None:
        for e in lst:
            self.add_genre_or_tag_helper(e.strip())
            pass
        return None

    def remove_genre_or_tag(self, e: str) -> None:
        if e in TAGS:
            if e in self.tags:
                self.tags.remove(e)
                pass
            pass
        else:
            if e in self.genres:
                self.genres.remove(e)
                pass
            pass
        return None

    def remove_genres_or_tags(self, lst: list) -> None:
        for e in lst:
            self.remove_genre_or_tag(e.strip())
            pass
        return None

    def get_language_ISO(self) -> str:
        return self.language_ISO

    def set_language_ISO(self, language_ISO: str) -> None:
        self.language_ISO = language_ISO
        return None

    def get_groups(self) -> list:
        return self.groups

    def add_groups(self, groups: list) -> None:
        for group in groups:
            self.add_group(group)
            pass
        return None

    def add_group(self, group: str) -> None:
        self.groups.append(group)
        return None

    def get_title(self) -> str:
        return self.title

    def set_title(self, title: str) -> None:
        self.title = title
        return None

    def get_number(self) -> str:
        return self.number

    def set_number(self, number: str) -> None:
        self.number = number
        return None

    def get_volume(self) -> str:
        return self.volume

    def set_volume(self, volume: str) -> None:
        self.volume = volume
        return None

    # def get_alternate_series(self) -> str:
    #     return self.alternate_series
    #
    # def set_alternate_series(self, alternate_series: str) -> None:
    #     self.alternate_series = alternate_series
    #     return None
    #
    # def get_alternate_number(self) -> str:
    #     return self.alternate_number
    #
    # def set_alternate_number(self, alternate_number: str) -> None:
    #     self.alternate_number = alternate_number
    #     return None
    #
    # def get_alternate_count(self) -> int:
    #     return self.alternate_count
    #
    # def set_alternate_count(self, alternate_count: int) -> None:
    #     self.alternate_count = alternate_count
    #     return None

    def get_summary(self) -> str:
        return self.summary

    def set_summary(self, summary: str) -> None:
        self.summary = summary
        return None

    def get_year(self) -> int:
        return self.year

    def set_year(self, year: int) -> None:
        self.year = year
        return None

    def get_month(self) -> int:
        return self.month

    def set_month(self, month: int) -> None:
        self.month = month
        return None

    def get_day(self) -> int:
        return self.day

    def set_day(self, day: int) -> None:
        self.day = day
        return None

    def get_authors(self) -> list:
        return self.authors

    def set_authors(self, authors: list) -> None:
        self.authors = authors
        return None

    def add_authors(self, authors: list) -> None:
        for author in authors:
            self.add_author(author)
            pass
        return None

    def add_author(self, author: str) -> None:
        self.authors.append(author)
        return None

    def get_artists(self) -> list:
        return self.artists

    def set_artists(self, artists: list) -> None:
        self.artists = artists
        return None

    def add_artists(self, artists: list) -> None:
        for artist in artists:
            self.add_artist(artist)
            pass
        return None

    def add_artist(self, artist: str) -> None:
        self.artists.append(artist)
        return None

    def get_inkers(self) -> list:
        return self.inkers

    def add_inkers(self, inkers: list) -> None:
        for inker in inkers:
            self.add_inker(inker)
            pass
        return None

    def add_inker(self, inker: str) -> None:
        self.inkers.append(inker)
        return None

    def get_colorists(self) -> list:
        return self.colorists

    def add_colorists(self, colorists: list) -> None:
        for colorist in colorists:
            self.add_colorist(colorist)
            pass
        return None

    def add_colorist(self, colorist: str) -> None:
        self.colorists.append(colorist)
        return None

    def get_letterers(self) -> list:
        return self.letterers

    def add_letterers(self, letterers: list) -> None:
        for letterer in letterers:
            self.add_letterer(letterer)
            pass
        return None

    def add_letterer(self, letterer: str) -> None:
        self.letterers.append(letterer)
        return None

    def get_cover_artists(self) -> list:
        return self.cover_artists

    def add_cover_artists(self, cover_artists: list) -> None:
        for cover_artist in cover_artists:
            self.add_cover_artist(cover_artist)
            pass
        return None

    def add_cover_artist(self, cover_artist: str) -> None:
        self.cover_artists.append(cover_artist)
        return None

    def get_editors(self) -> list:
        return self.editors

    def add_editors(self, editors: list) -> None:
        for editor in editors:
            self.add_editor(editor)
            pass
        return None

    def add_editor(self, editor: str) -> None:
        self.editors.append(editor)
        return None

    def get_translators(self) -> list:
        return self.translators

    def add_translators(self, translators: list) -> None:
        for translator in translators:
            self.add_translator(translator)
            pass
        return None

    def add_translator(self, translator: str) -> None:
        self.translators.append(translator)
        return None

    def get_urls(self) -> list:
        return self.urls

    def add_urls(self, urls: list) -> None:
        for url in urls:
            self.add_url(url)
            pass
        return None

    def add_url(self, url: str) -> None:
        self.urls.append(url)
        return None

    def get_page_count(self) -> int:
        return self.page_count

    def set_page_count(self, page_count: int) -> None:
        self.page_count = page_count
        return None

    def get_format(self) -> str:
        return self.format

    def set_format(self, fmt: str) -> None:
        self.format = fmt
        return None

    def is_black_and_white(self) -> None:
        self.black_and_white = True
        return None

    def get_characters(self) -> list:
        return self.characters

    def add_characters(self, characters: list) -> None:
        for character in characters:
            self.add_character(character)
            pass
        return None

    def add_character(self, character: str) -> None:
        self.characters.append(character)
        return None

    def get_teams(self) -> list:
        return self.teams

    def add_teams(self, teams: list) -> None:
        for team in teams:
            self.add_team(team)
            pass
        return None

    def add_team(self, team: str) -> None:
        self.teams.append(team)
        return None

    def get_locations(self) -> list:
        return self.locations

    def add_locations(self, locations: list) -> None:
        for location in locations:
            self.add_location(location)
            pass
        return None

    def add_location(self, location: str) -> None:
        self.locations.append(location)
        return None

    def get_main_character_or_team(self) -> str:
        return self.main_character_or_team

    def set_main_character_or_team(self, main_character_or_team: str) -> None:
        self.main_character_or_team = main_character_or_team
        return None

    def get_story_arc(self) -> str:
        return self.story_arc

    def set_story_arc(self, story_arc: str) -> None:
        self.story_arc = story_arc
        return None

    def get_story_arc_number(self) -> str:
        return self.story_arc_number

    def set_story_arc_number(self, story_arc_number: str) -> None:
        self.story_arc_number = story_arc_number
        return None

    def get_age_rating(self) -> str:
        return self.age_rating

    def set_age_rating(self, age_rating: int) -> None:
        self.age_rating = KOMGA_AGE_RATING[age_rating]
        return None

    def get_age_rating_publisher(self) -> str:
        return self.age_rating_publisher

    def set_age_rating_publisher(self, age_rating_publisher: str) -> None:
        self.age_rating_publisher = age_rating_publisher
        return None

    def get_community_rating(self) -> float:
        return self.community_rating

    def set_community_rating(self, community_rating: float) -> None:
        self.community_rating = community_rating
        return None

    def get_review(self) -> str:
        return self.review

    def set_review(self, review: str) -> None:
        self.review = review
        return None

    def get_isbn(self) -> str:
        return self.isbn

    def set_isbn(self, isbn: str) -> None:
        self.isbn = isbn
        return None

    def get_notes(self) -> str:
        return self.notes

    def set_notes(self, notes: str) -> None:
        self.notes = notes
        return None

    def get_scan_information(self) -> str:
        return self.scan_information

    def set_scan_information(self, scan_information: str) -> None:
        self.scan_information = scan_information
        return None

    def check_conflicting_genres_and_tags(self) -> None:
        self.remove_genres_or_tags(["Crossdressing", "Magical Sex Change"])
        for (genre, series_lst) in SERIES_XDRESSING_MAGICAL_SEX_CHANGE.items():
            if self.series in series_lst:
                self.add_genre_or_tag(genre)
                pass
            pass
        return None

    def add_sports_tag(self) -> None:
        for (genre, series_lst) in SERIES_SPORTS.items():
            if self.series in series_lst:
                self.add_genre_or_tag(genre)
                pass
            pass
        return None

    def get_xml_data(self) -> str:
        xml_data: str = (
            f"<?xml version='1.0' encoding='utf-8'?>\n"
            f"<ComicInfo>\n"
            f"\t<Series>{self.series}</Series>\n"
        )
        strs_as_dict: dict = {"JapaneseTitle": self.japanese_title,
                              "Status": self.status}
        for (k, v) in strs_as_dict.items():
            if v != "":
                xml_data: str = (
                    f"{xml_data}"
                    f"\t<{k}>{v}</{k}>\n"
                )
                pass
            pass
        if self.count > -1:
            xml_data: str = (
                f"{xml_data}"
                f"\t<Count>{self.count}</Count>\n"
            )
            pass
        # strs_as_dict: dict = {"AlternateSeries": self.alternate_series,
        #                       "AlternateNumber": self.alternate_number}
        # for (k, v) in strs_as_dict.items():
        #     if v != "":
        #         xml_data: str = (
        #             f"{xml_data}"
        #             f"\t<{k}>{v}</{k}>\n"
        #         )
        #         pass
        #     pass
        # if self.alternate_count > -1:
        #     xml_data: str = (
        #         f"{xml_data}"
        #         f"\t<AlternateCount>{self.alternate_count}</AlternateCount>\n"
        #     )
        #     pass
        if self.imprint != "":
            if self.imprint != self.publisher:
                xml_data: str = (
                    f"{xml_data}"
                    f"\t<Publisher>{self.publisher} ({self.imprint})</Publisher>\n"
                    f"\t<Imprint>{self.imprint}</Imprint>\n"
                )
                pass
            else:
                xml_data: str = (
                    f"{xml_data}"
                    f"\t<Publisher>{self.publisher}</Publisher>\n"
                    f"\t<Imprint>{self.imprint}</Imprint>\n"
                )
                pass
            pass
        else:
            xml_data: str = (
                f"{xml_data}"
                f"\t<Publisher>{self.publisher}</Publisher>\n"
            )
            pass
        lsts_as_dict: dict = {"Genre": self.genres, "Tags": self.tags}
        for (k, v) in lsts_as_dict.items():
            if len(v) > 0:
                v.sort()
                sep: str = ", "
                xml_data: str = (
                    f"{xml_data}"
                    f"\t<{k}>{utils.convert_lst_to_str(v, sep)}</{k}>\n"
                )
                pass
            pass
        if self.language_ISO != "":
            xml_data: str = (
                f"{xml_data}"
                f"\t<LanguageISO>{self.language_ISO}</LanguageISO>\n"
            )
            pass
        strs_as_dict: dict = {"LanguageISO": self.language_ISO}
        for (k, v) in strs_as_dict.items():
            if v != "":
                xml_data: str = (
                    f"{xml_data}"
                    f"\t<{k}>{v}</{k}>\n"
                )
                pass
            pass
        if len(self.groups) > 0:
            sep: str = ", "
            lst_to_str: str = utils.convert_lst_to_str(self.groups, sep)
            xml_data: str = (
                f"{xml_data}"
                f"\t<SeriesGroup>{lst_to_str}</SeriesGroup>\n"
            )
            pass
        xml_data: str = (
            f"{xml_data}"
            f"\t<Title>{self.title}</Title>\n"
            f"\t<Number>{self.number}</Number>\n"
        )
        strs_as_dict: dict = {"Volume": self.volume,
                              # "AlternateSeries": self.alternate_series,
                              # "AlternateNumber": self.alternate_number
                              }
        for (k, v) in strs_as_dict.items():
            if v != "":
                xml_data: str = (
                    f"{xml_data}"
                    f"\t<{k}>{v}</{k}>\n"
                )
                pass
            pass
        # if self.alternate_count > -1:
        #     xml_data: str = (
        #         f"{xml_data}"
        #         f"\t<AlternateCount>{self.alternate_count}</AlternateCount>\n"
        #     )
        #     pass
        xml_data: str = (
            f"{xml_data}"
            f"\t<Summary>{self.summary}</Summary>\n"
            f"\t<Year>{self.year}</Year>\n"
            f"\t<Month>{self.month}</Month>\n"
            f"\t<Day>{self.day}</Day>\n"
        )
        lsts_as_dict: dict = {"Writer": self.authors,
                              "Penciller": self.artists,
                              "Inker": self.inkers, "Colorist": self.colorists,
                              "Letterer": self.letterers,
                              "CoverArtist": self.cover_artists,
                              "Editor": self.editors,
                              "Translator": self.translators,
                              "Web": self.urls}
        for (k, v) in lsts_as_dict.items():
            if len(v) > 0:
                v.sort()
                sep: str = ", "
                if k == "Web":
                    sep = " "
                    pass
                xml_data: str = (
                    f"{xml_data}"
                    f"\t<{k}>{utils.convert_lst_to_str(v, sep)}</{k}>\n"
                )
                pass
            pass
        if self.page_count > 0:
            xml_data: str = (
                f"{xml_data}"
                f"\t<PageCount>{self.page_count}</PageCount>\n"
            )
            pass
        if self.format != "":
            xml_data: str = (
                f"{xml_data}"
                f"\t<Format>{self.format}</Format>\n"
            )
            pass
        bool_as_dict: dict = {"BlackAndWhite": [self.black_and_white, "Yes"]}
        for (k, v) in bool_as_dict.items():
            if v[0]:
                xml_data: str = (
                    f"{xml_data}"
                    f"\t<{k}>{v[1]}</{k}>\n"
                )
                pass
            pass
        xml_data: str = (
            f"{xml_data}"
            f"\t<Manga>YesAndRightToLeft</Manga>\n"
        )
        lsts_as_dict: dict = {"Characters": self.characters,
                              "Teams": self.teams,
                              "Locations": self.locations}
        for (k, v) in lsts_as_dict.items():
            if len(v) > 0:
                v.sort()
                sep: str = ", "
                xml_data: str = (
                    f"{xml_data}"
                    f"\t<{k}>{utils.convert_lst_to_str(v, sep)}</{k}>\n"
                )
                pass
            pass
        strs_as_dict: dict = {
            "MainCharacterOrTeam": self.main_character_or_team,
            "StoryArc": self.story_arc,
            "StoryArcNumber": self.story_arc_number,
        }
        for (k, v) in strs_as_dict.items():
            if v != "":
                xml_data: str = (
                    f"{xml_data}"
                    f"\t<{k}>{v}</{k}>\n"
                )
                pass
            pass
        field: str = "AgeRatingPublisher"
        xml_data: str = (
            f"{xml_data}"
            f"\t<AgeRating>{self.age_rating}</AgeRating>\n"
            f"\t<{field}>{self.age_rating_publisher}</{field}>\n"
        )
        if self.community_rating > -1.0:
            field: str = "CommunityRating"
            xml_data: str = (
                f"{xml_data}"
                f"\t<{field}>{self.community_rating}</{field}>\n"
            )
            pass
        if self.review != "":
            xml_data: str = (
                f"{xml_data}"
                f"\t<Review>{self.review}</Review>\n"
            )
            pass
        xml_data: str = (
            f"{xml_data}"
            f"\t<GTIN>{self.isbn}</GTIN>\n"
        )
        strs_as_dict: dict = {"Notes": self.notes,
                              "ScanInformation": self.scan_information}
        for (k, v) in strs_as_dict.items():
            if v != "":
                xml_data: str = (
                    f"{xml_data}"
                    f"\t<{k}>{v}</{k}>\n"
                )
                pass
            pass
        xml_data: str = (
            f"{xml_data}"
            f"</ComicInfo>"
        )
        return xml_data

    pass
