import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import argparse
from jinja2 import Template
from matplotlib import rc


def set_matplotlib() -> None:
    if sys.platform == "linux":  # Windows
        rc("font", family="NanumBarunGothic")
    elif sys.platform == "darwin":  # MacOS
        rc("font", family="AppleGothic")

    plt.rcParams["axes.unicode_minus"] = False

parser = argparse.ArgumentParser()
parser.add_argument("file", type=str, help="input .csv file")
args = parser.parse_args()

# check file
if not args.file.endswith(".csv"):
    parser.error("only .csv file supported")
set_matplotlib()

with open("template.md") as f:
    data = f.read()

covid = pd.read_csv("covid-19.csv")
covid["date"] = pd.to_datetime((covid["year"]*10000+covid["month"]*100+covid["day"]).apply(str), format="%Y%m%d") 
tm = Template(data)
td = datetime.datetime.now()

def weekday_region(region, dayweek):
    covid19 = covid[(covid['type']==region) & (covid["date"].dt.dayofweek == dayweek)]['cnt']
    return covid19.sum() 

def _draw_chart(df: pd.DataFrame):
    df.pivot_table(values="cnt",index="day", columns="type", aggfunc="sum").plot(
        kind="bar"
    )
    plt.title("covid 현황")

    file_path = datetime.datetime.now().strftime("%Y%m%d_covid.png")
    plt.savefig(file_path, dpi=300)

    return file_path

file_path = _draw_chart(covid)

args = {
    "year" : td.year,
    "month" : td.month,
    "day" : td.day,
    "total_covid" : covid[covid['type']=='합계']['cnt'].sum(),
    "seoul_covid" : covid[covid['type']=='서울']['cnt'].sum(),
    "start_date" : min(covid["date"]).strftime("%Y-%m-%d"),
    "end_date" : max(covid["date"]).strftime("%Y-%m-%d"),
    "total_mon" : weekday_region('합계',0),
    "seoul_mon" : weekday_region('서울',0),
    "total_tus" : weekday_region('합계',1),
    "seoul_tus" : weekday_region('서울',1),
    "total_wed" : weekday_region('합계',2),
    "seoul_wed" : weekday_region('서울',2),
    "total_thr" : weekday_region('합계',3),
    "seoul_thr" : weekday_region('서울',3),
    "total_fri" : weekday_region('합계',4),
    "seoul_fri" : weekday_region('서울',4),
    "total_sat" : weekday_region('합계',5),
    "seoul_sat" : weekday_region('서울',5),
    "total_sun" : weekday_region('합계',6),
    "seoul_sun" : weekday_region('서울',6),
    "graph" : f"![]({file_path})",
}

msg = tm.render(**args)

with open("result.md", "w") as f:
    f.write(msg)
    
