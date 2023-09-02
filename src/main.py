"""
Author: Rayla Kurosaki

GitHub: https://github.com/rkp1503
"""

import math
import os
import shutil
import sys
import zipfile

import numpy as np
import pandas as pd

PRESORTED: list = ["High School of the Dead", "Mayo Chiki!", "Strobe Edge",
                   "Assorted Entanglements", "Citrus+",
                   "I Think I Turned My Childhood Friend Into a Girl",
                   "Pokémon Adventures", "", ]
SERIES: list = ["Higurashi When They Cry (Main Series)",
                "Higurashi When They Cry (Sequel 1)",
                "Higurashi When They Cry (Sequel 2)",
                "Higurashi When They Cry (Side Stories)", "Yu-Gi-Oh! (Series)",
                "", ]
BATO: list = ["Corpse Party - Blood Covered", "Corpse Party - Book of Shadows",
              "", ]


def get_volume_chapter_details(path_to_manga: str) -> tuple[list, list] | None:
    lst_vols: list = []
    lst_first_ch: list = []
    path_to_data: str = os.path.join(path_to_manga, "data.csv")
    if os.path.exists(path_to_data):
        dataframe = pd.read_csv(path_to_data)
        for index, row in dataframe.iterrows():
            lst_vols.append(row["Vol"])
            if pd.isna(row["First Ch"]):
                lst_first_ch.append(np.inf)
                pass
            else:
                lst_first_ch.append(row["First Ch"])
                pass
            pass
        lst_vols: list = reformat_volume_numbers(lst_vols)
        if not isinstance(lst_first_ch[0], int):
            lst_first_ch: list = reformat_chapter_numbers(lst_first_ch)
            pass
        return lst_vols, lst_first_ch
    else:
        return None
    pass


def get_padding(curr_vol, last_vol) -> str:
    if curr_vol < 1:
        curr_vol = 1
    return "0" * (math.floor(math.log10(last_vol)) - math.floor(
        math.log10(curr_vol)))


def reformat_volume_numbers(temp_lst: list) -> list:
    lst_vols: list = []
    last_vol_num: str = str(temp_lst[-1])
    if "-" in last_vol_num:
        last_vol_num: float = float(last_vol_num.split("-")[-1])
        pass
    else:
        last_vol_num: float = float(last_vol_num)
        pass
    if isinstance(temp_lst[0], int):
        for vol_num in temp_lst:
            padding: str = get_padding(int(vol_num), last_vol_num)
            lst_vols.append(f"{padding}{vol_num}")
            pass
        pass
    elif isinstance(temp_lst[0], float):
        for vol_num in temp_lst:
            if str(vol_num).endswith(".0"):
                vol_num: int = int(vol_num)
                pass
            padding: str = get_padding(vol_num, last_vol_num)
            lst_vols.append(f"{padding}{vol_num}")
            pass
        pass
    elif isinstance(temp_lst[0], str):
        for e in temp_lst:
            vol_nums: list = str(e).split("-")
            if len(vol_nums) == 2:
                vol_num_a, vol_num_b = vol_nums
                vol_num_a: float = float(vol_num_a)
                if str(vol_num_a).endswith(".0"):
                    vol_num_a: int = int(vol_num_a)
                    pass
                padding_a: str = get_padding(vol_num_a, last_vol_num)
                vol_num_b: float = float(vol_num_b)
                if str(vol_num_b).endswith(".0"):
                    vol_num_b: int = int(vol_num_b)
                    pass
                padding_b: str = get_padding(vol_num_b, last_vol_num)
                lst_vols.append(
                    f"{padding_a}{vol_num_a}-{padding_b}{vol_num_b}")
                pass
            else:
                vol_num: float = float(vol_nums[0])
                if str(vol_num).endswith(".0"):
                    vol_num: int = int(vol_num)
                    pass
                padding: str = get_padding(vol_num, last_vol_num)
                lst_vols.append(f"{padding}{vol_num}")
                pass
            pass
        pass
    return lst_vols


def reformat_chapter_numbers(temp_lst: list) -> list:
    lst_first_ch: list = []
    for first_ch in temp_lst:
        if (not isinstance(first_ch, int)) and (str(first_ch).endswith(".0")):
            first_ch: int = int(str(first_ch).split(".")[0])
            pass
        lst_first_ch.append(first_ch)
        pass
    return lst_first_ch


def add_padding_to_chapters(path_to_manga: str) -> None:
    for folder in os.listdir(path_to_manga):
        if "Chapter" in folder:
            src: str = os.path.join(path_to_manga, folder)
            manga_title: str = folder.split(" Chapter ")[0]
            ch_num: str = folder.split(" Chapter ")[-1]
            padding: str = get_padding(float(ch_num), 100_000)
            new_folder: str = f"{manga_title} Chapter {padding}{ch_num}"
            dst: str = os.path.join(path_to_manga, new_folder)
            os.rename(src, dst)
            pass
        pass
    return None


def convert_chapters_to_volumes(path_to_manga: str, lst_vols: list,
                                lst_first_ch: list, source="MangaSee",
                                presorted=False) -> None:
    i: int = 0
    curr_first_ch: float = float(lst_first_ch[0]) if len(
        lst_first_ch) == 1 else float(lst_first_ch[i + 1])
    if presorted:
        vol_c: int = 0
        for item_1 in os.listdir(path_to_manga):
            if "Chapter" in item_1:
                vol_name: str = f"Volume {lst_vols[vol_c]}"
                book_name: str = f"{vol_name}.cbz"
                path_to_vol: str = os.path.join(path_to_manga, vol_name)
                path_to_book: str = os.path.join(path_to_manga, book_name)
                vol_dir_exist: bool = os.path.exists(path_to_vol)
                book_exist: bool = os.path.exists(path_to_book)
                if not (vol_dir_exist or book_exist):
                    os.makedirs(path_to_vol)
                    pass
                path_to_chapter: str = os.path.join(path_to_manga, item_1)
                for item_2 in os.listdir(path_to_chapter):
                    src: str = os.path.join(path_to_chapter, item_2)
                    page_name: str = ""
                    if source == "Bato":
                        ext: str = item_2.split(".")[-1]
                        page_num: str = item_2.split("_")[0]
                        page_name: str = f"{lst_vols[vol_c]}-{page_num}.{ext}"
                        pass
                    else:
                        if "-" in item_2:
                            page_name: str = item_2.split("_")[-1]
                            pass
                        pass
                    if page_name != "":
                        dst: str = os.path.join(path_to_vol, page_name)
                        shutil.move(src, dst)
                        pass
                    pass
                vol_c += 1
                shutil.rmtree(path_to_chapter)
                pass
            pass
        pass
    else:
        for item_1 in os.listdir(path_to_manga):
            if "Chapter" in item_1:
                ch_num: str = item_1.split(" Chapter ")[-1]
                while (float(ch_num) >= curr_first_ch) and (
                        i + 1 < len(lst_vols)):
                    i += 1
                    if i + 1 < len(lst_vols):
                        curr_first_ch: list = lst_first_ch[i + 1]
                        pass
                    pass
                book_name: str = f"Volume {lst_vols[i]}"
                path_to_vol: str = os.path.join(path_to_manga, book_name)
                path_to_cbz: str = os.path.join(path_to_vol, ".cbz")
                vol_dir_exist: bool = os.path.exists(path_to_vol)
                vol_cbz_exist: bool = os.path.exists(path_to_cbz)
                if not (vol_dir_exist or vol_cbz_exist):
                    os.makedirs(path_to_vol)
                    pass
                path_to_chapter: str = os.path.join(path_to_manga, item_1)
                for item_2 in os.listdir(path_to_chapter):
                    src: str = os.path.join(path_to_chapter, item_2)
                    page_name: str = ""
                    if source == "Bato":
                        if "logo-batoto" not in item_2:
                            ext: str = item_2.split(".")[-1]
                            page_num: str = item_2.split("_")[0]
                            page_name: str = f"{ch_num}-{page_num}.{ext}"
                            pass
                        pass
                    else:
                        if "-" in item_2:
                            page_name: str = item_2.split("_")[-1]
                            pass
                        pass
                    if page_name != "":
                        dst: str = os.path.join(path_to_vol, page_name)
                        shutil.move(src, dst)
                        pass
                    pass
                shutil.rmtree(path_to_chapter)
                pass
            pass
        pass
    return None


def get_volume_covers(path_to_manga: str) -> None:
    path_to_vol_covers: str = os.path.join(path_to_manga, "Volume Covers")
    if not os.path.exists(path_to_vol_covers):
        os.makedirs(path_to_vol_covers)
        pass
    for item in os.listdir(path_to_manga):
        cond_1: bool = "Volume" in item
        cond_2: bool = item != "Volume Covers"
        cond_3: bool = not (item.endswith(".zip") or item.endswith(".cbz"))
        if cond_1 and cond_2 and cond_3:
            path_to_vol: str = os.path.join(path_to_manga, item)
            src: str = os.path.join(path_to_vol, os.listdir(path_to_vol)[0])
            vol: str = item.split(" ")[-1]
            ext: str = src.split(".")[-1]
            filename: str = f"volume-cover-{vol}.{ext}"
            dst: str = os.path.join(path_to_vol_covers, filename)
            if not os.path.exists(dst):
                shutil.copy(src, dst)
                pass
            pass
        pass
    return None


def convert_folders_to_cbz(path_to_manga: str) -> None:
    for item in os.listdir(path_to_manga):
        if ("Volume" in item) and (item != "Volume Covers"):
            # Zip the file
            path_to_zip: str = os.path.join(path_to_manga, f"{item}.zip")
            with zipfile.ZipFile(path_to_zip, mode="w") as zip_file:
                for folderName, subfolders, filenames in os.walk(item):
                    for filename in filenames:
                        path_to_file: str = os.path.join(folderName, filename)
                        file_base_name: str = os.path.basename(path_to_file)
                        zip_file.write(path_to_file, file_base_name)
                        pass
                    pass
                pass
            # Change the extension from .zip to .cbz
            path_to_cbz: str = os.path.join(path_to_manga, f"{item}.cbz")
            os.rename(path_to_zip, path_to_cbz)
            # Remove the directory
            shutil.rmtree(os.path.join(path_to_manga, item))
            pass
        pass
    return None


def main() -> None:
    path_to_lib: str = sys.argv[1]
    data_file: str = "data.csv"
    csv_src: str = os.path.join(os.path.dirname(path_to_lib), data_file)
    for manga in os.listdir(path_to_lib):
        if manga not in SERIES:
            path_to_manga: str = os.path.join(path_to_lib, manga)
            path_to_data: str = os.path.join(path_to_manga, data_file)
            if os.path.exists(path_to_data):
                print(manga)
                data = get_volume_chapter_details(path_to_manga)
                if data is not None:
                    add_padding_to_chapters(path_to_manga)
                    lst_vols, lst_first_ch = data
                    if manga in BATO:
                        if manga in PRESORTED:
                            convert_chapters_to_volumes(path_to_manga,
                                                        lst_vols, lst_first_ch,
                                                        source="Bato",
                                                        presorted=True)
                            pass
                        else:
                            convert_chapters_to_volumes(path_to_manga,
                                                        lst_vols, lst_first_ch,
                                                        source="Bato")
                            pass
                        pass
                    else:
                        if manga in PRESORTED:
                            convert_chapters_to_volumes(path_to_manga,
                                                        lst_vols, lst_first_ch,
                                                        presorted=True)
                            pass
                        else:
                            convert_chapters_to_volumes(path_to_manga,
                                                        lst_vols, lst_first_ch)
                            pass
                        pass
                    get_volume_covers(path_to_manga)
                    convert_folders_to_cbz(path_to_manga)
                    pass
                else:
                    print(f"No data given for '{manga}'. "
                          f"Skipping this series...")
                    pass
                pass
            else:
                print(f"Missing data.csv for '{manga}'. "
                      f"Skipping this series...")
                csv_dst: str = os.path.join(path_to_manga, "data.csv")
                shutil.copyfile(csv_src, csv_dst)
                pass
            pass
        pass
    return None


if __name__ == '__main__':
    main()
    pass
