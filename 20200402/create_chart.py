""".csv 파일 및 옵션 값을 받아 해당 옵션에 맞는 차트 그래프 생성

python create_chart.py [--type 차트타입] [--stations 해당지역] apt_price.csv
"""
import argparse
import sys
import time
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc
from argparse import Namespace


def set_matplotlib() -> None:
    if sys.platform == 'linux':  # Windows
        rc('font', family='NanumBarunGothic')
    elif sys.platform == 'darwin':  # MacOS
        rc('font', family='AppleGothic')

    plt.rcParams['axes.unicode_minus'] = False


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str,
                        help ='input csv file')
    parser.add_argument('-t', '--type', type=str, choices=['line', 'bar', 'pie'], default='bar')
    parser.add_argument('-s', '--stations', type=str, help='stations name with `,`')

    return parser


def check_args(parser: argparse.ArgumentParser) -> Namespace:
    args = parser.parse_args()

    # check file
    if not args.file.endswith('.csv'):
        parser.error('only .csv file supported')

    valid_stations = [
        '서울', '부산', '대구', '광주', '대전', '울산', '제주'
    ]

    # check stations
    if args.stations:
        stations = list(map(lambda x: x.strip(), args.stations.split(',')))
        for station in stations:
            if station not in valid_stations:
                parser.error(f'"{station}" not in {valid_stations}')

        args.stations = stations

    return args


def draw_chart(type_: str, df: pd.DataFrame) -> str:
    filename = ''

    if type_ == 'bar': 
        filename = _draw_bar_chart(df)
    elif type_ == 'line':
        filename = _draw_line_chart(df)
    elif type_ == 'pie':
        filename = _draw_pie_chart(df)

    return filename


def _get_time_str() -> str:
    return str(int(time.time()))


def _draw_bar_chart(df: pd.DataFrame) :
    df.pivot_table(values='분양가격(㎡)', index='지역명', columns ='규모구분', aggfunc='mean').plot(kind='bar')
    plt.title('지역별 평균 분양가격')
    return 'bar_chart_' + _get_time_str()


def _draw_line_chart(df: pd.DataFrame):
    df.pivot_table(values='분양가격(㎡)', index='지역명', columns ='규모구분', aggfunc='mean').plot(kind='line')
    plt.title('지역별 평균 분양가격')
    return 'line_chart_' + _get_time_str()

    
def _draw_pie_chart(df: pd.DataFrame) :
    df['월'].value_counts().plot.pie(autopct='%.2f%%')
    plt.title('월별 데이터 비율')
    return 'pie_chart_' + _get_time_str()


def save_chart_png(filename: str):
    plt.savefig(filename + '.png', dpi=300)


def main():
    set_matplotlib()
    parser = get_parser()
    args = check_args(parser)

    df = pd.read_csv(args.file, encoding='euc-kr')
    df['분양가격(㎡)'] = pd.to_numeric(df['분양가격(㎡)'], errors='coerce')
    df['분양가격(㎡)'].fillna(df['분양가격(㎡)'].mean())
            
    if args.stations:
        df = df[df['지역명'].isin(args.stations)]

    filename = draw_chart(args.type, df)
    save_chart_png(filename)

if __name__ == "__main__":
    main()
