""".csv 파일을 인자로 받아 막대그래프 .png 파일을 생성하는 모듈

python create_barchar.py apt_price.py
"""
import sys

import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["axes.unicode_minus"] = False


def cmd_help():
    msg = f"{sys.argv[0]} <csv file>"
    print(msg)
    sys.exit(1)


def main():
    if len(sys.argv) > 2:
        cmd_help()

    csv_file = sys.argv[1]
    if not csv_file.endswith(".csv"):
        cmd_help()

    data = pd.read_csv(csv_file, encoding="euc-kr")
    data["분양가격(㎡)"] = pd.to_numeric(data["분양가격(㎡)"], errors="coerce")
    data["분양가격(㎡)"].fillna(data["분양가격(㎡)"].mean())
    data.pivot_table(
        values="분양가격(㎡)", index="지역명", columns="규모구분", aggfunc="mean"
    ).plot(kind="bar")
    plt.title("지역별 평균 분양가격")
    plt.savefig("img" + ".png", dpi=300)


if __name__ == "__main__":
    main()
