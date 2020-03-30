import argparse
import datetime
import sys

import matplotlib.pyplot as plt
import pandas as pd
from jinja2 import Template
from matplotlib import rc


class DayOfWeek:
    mon = 0
    tue = 1
    wed = 2
    thur = 3
    fri = 4
    sat = 5
    sun = 6


def set_matplotlib() -> None:
    if sys.platform == "linux":  # Windows
        rc("font", family="NanumBarunGothic")
    elif sys.platform == "darwin":  # MacOS
        rc("font", family="AppleGothic")

    plt.rcParams["axes.unicode_minus"] = False


def weekday_region(df: pd.DataFrame, region: str, dayweek: str) -> int:
    covid19 = df[(df["type"] == region) & (df["date"].dt.dayofweek == dayweek)]["cnt"]
    return covid19.sum()


def save_barchart(df: pd.DataFrame):
    dff = df.copy()
    dff.pivot_table(values="cnt", index="day", columns="type", aggfunc="sum").plot(
        kind="bar"
    )
    plt.title("covid 현황")

    file_path = datetime.datetime.now().strftime("%Y%m%d_covid.png")
    plt.savefig(file_path, dpi=300)

    return file_path


def main():
    # setting parser
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=str, help="input .csv file")
    args = parser.parse_args()

    # check file
    if not args.file.endswith(".csv"):
        parser.error("only .csv file supported")

    # handling data
    covid = pd.read_csv("covid-19.csv")
    covid["date"] = pd.to_datetime(
        (covid["year"] * 10000 + covid["month"] * 100 + covid["day"]).apply(str),
        format="%Y%m%d",
    )

    # settig matplotlib
    set_matplotlib()

    # setting variable
    today = datetime.datetime.now()
    file_path = save_barchart(covid)
    args = {
        "year": today.year,
        "month": today.month,
        "day": today.day,
        "total_covid": covid[covid["type"] == "합계"]["cnt"].sum(),
        "seoul_covid": covid[covid["type"] == "서울"]["cnt"].sum(),
        "start_date": min(covid["date"]).strftime("%Y-%m-%d"),
        "end_date": max(covid["date"]).strftime("%Y-%m-%d"),
        "total_mon": weekday_region(covid, "합계", DayOfWeek.mon),
        "seoul_mon": weekday_region(covid, "서울", DayOfWeek.mon),
        "total_tus": weekday_region(covid, "합계", DayOfWeek.tue),
        "seoul_tus": weekday_region(covid, "서울", DayOfWeek.tue),
        "total_wed": weekday_region(covid, "합계", DayOfWeek.wed),
        "seoul_wed": weekday_region(covid, "서울", DayOfWeek.wed),
        "total_thr": weekday_region(covid, "합계", DayOfWeek.thur),
        "seoul_thr": weekday_region(covid, "서울", DayOfWeek.thur),
        "total_fri": weekday_region(covid, "합계", DayOfWeek.fri),
        "seoul_fri": weekday_region(covid, "서울", DayOfWeek.fri),
        "total_sat": weekday_region(covid, "합계", DayOfWeek.sat),
        "seoul_sat": weekday_region(covid, "서울", DayOfWeek.sat),
        "total_sun": weekday_region(covid, "합계", DayOfWeek.sun),
        "seoul_sun": weekday_region(covid, "서울", DayOfWeek.sun),
        "graph": f"![]({file_path})",
    }

    # read template
    with open("template.md") as f:
        data = f.read()

    # rendering template
    tm = Template(data)
    msg = tm.render(**args)

    # write file
    with open("result.md", "w") as f:
        f.write(msg)


if __name__ == "__main__":
    main()
