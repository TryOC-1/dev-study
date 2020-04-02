""".csv 파일 및 옵션 값을 받아 해당 옵션에 맞는 차트 그래프 생성

python create_chart.py [--type 차트타입] [--stations 해당지역] apt_price.csv
"""

import argparse
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font', family='AppleGothic')

plt.rcParams['axes.unicode_minus'] = False

def read_file(csvfile) :
    return pd.read_csv(csvfile, encoding='euc-kr')


def handling(data):
    data = pd.DataFrame(data)
    data['분양가격(㎡)'] = pd.to_numeric(data['분양가격(㎡)'], errors='coerce')
    data['분양가격(㎡)'].fillna(data['분양가격(㎡)'].mean())
    return data


def bar_chart(data) :
    data.pivot_table(values='분양가격(㎡)', index='지역명', columns ='규모구분', aggfunc='mean').plot(kind='bar')
    plt.title('지역별 평균 분양가격')
    

def pie_chart(data) :
    data['월'].value_counts().plot.pie(autopct='%.2f%%')
    plt.title('월별 데이터 비율')


def save_png(data):
    plt.savefig( args.file.split('.')[0]+'.png', dpi=300)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str,
                        help ='input csv file')
    parser.add_argument('--bar', action='store_true',
                        help ='bar chart')
    parser.add_argument('--pie', action='store_true',
                        help ='pie chart')
    args = parser.parse_args()
    data = read_file(args.file)
    data = handling(data)
    if args.bar : 
        bar_chart(data)
    elif args.pie :
        pie_chart(data)

    save_png(data)