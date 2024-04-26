"""
Author: Rayla Kurosaki

GitHub: https://github.com/rkp1503
"""

MONTH_CONVERSION: dict = {
    "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7,
    "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12
}

MONTH_CONVERSION_FULL: dict = {
    "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
    "July": 7, "August": 8, "September": 9, "October": 10, "November": 11,
    "December": 12
}

PERSON_NAME_CONVERSION: dict = {
    "Ryukishi 07": "Ryukishi07"
}


def convert_lst_to_str(lst: list, sep: str) -> str:
    string: str = f""
    for e in lst:
        string += e
        if e != lst[-1]:
            string += sep
            pass
        pass
    return string


def convert_name(name: str, jp_fmt: bool) -> str:
    if len(name.split(" ")) == 1:
        return name.capitalize()
    else:
        if jp_fmt:
            last_name: str = name.split(" ")[0]
            first_name: str = name.split(" ")[1]
            pass
        else:
            first_name: str = name.split(" ")[0]
            last_name: str = name.split(" ")[1]
            pass
        return f"{last_name.upper()} {first_name.capitalize()}"
    pass
