""".csv 파일을 인자로 받아 막대그래프 .png 파일을 생성하는 모듈

python create_barchar.py apt_price.py
"""
import argparse
<<<<<<< HEAD
import sys

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import rc

if sys.platform == "linux":  # Windows
    rc("font", family="NanumBarunGothic")
elif sys.platform == "darwin":  # MacOS
    rc("font", family="AppleGothic")

plt.rcParams["axes.unicode_minus"] = False


def read_file(csvfile):
    return pd.read_csv(csvfile, encoding="euc-kr")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=str, help="input csv file")
    args = parser.parse_args()
    data = read_file(args.file)
    if args.file.split(".")[-1] == "csv":
        data = pd.DataFrame(data)
        data["분양가격(㎡)"] = pd.to_numeric(data["분양가격(㎡)"], errors="coerce")
        data["분양가격(㎡)"].fillna(data["분양가격(㎡)"].mean())
        data.pivot_table(
            values="분양가격(㎡)", index="지역명", columns="규모구분", aggfunc="mean"
        ).plot(kind="bar")
        plt.title("지역별 평균 분양가격")
        plt.savefig(args.file.split(".")[0] + ".png", dpi=300)
    else:
        parser.print_help()
=======
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rc
rc('font', family='AppleGothic')

plt.rcParams['axes.unicode_minus'] = False

def read_file(csvfile):
    return pd.read_csv(csvfile, encoding='euc-kr')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str,
                        help ='input csv file')
    args = parser.parse_args()
    data = read_file(args.file)
    if args.file.split('.')[-1] == 'csv' :
        data = pd.DataFrame(data)
        data['분양가격(㎡)'] = pd.to_numeric(data['분양가격(㎡)'], errors='coerce')
        data['분양가격(㎡)'].fillna(data['분양가격(㎡)'].mean())
        data.pivot_table(values='분양가격(㎡)', index='지역명', columns ='규모구분', aggfunc='mean').plot(kind='bar')
        plt.title('지역별 평균 분양가격')
        plt.savefig(args.file.split('.')[0] + '.png', dpi=300)
    else :
        parser.print_help()


>>>>>>> create_barchart
