# 명령행 매개변수에서 검색 키워드를 가져온다.
# 검색결과 페이지를 검색한다.
# 각 결과를 새 브라우저 탭으로 연다.

# sys.argv로부터 명령행 매개변수 입력하기
# requests 모듈로 검색 결과 페이지를 가져오기
# 각 검색 결과에 대한 링크 찾기
# 웹 브라우저를 열고 webbrowser.open() 함수 호출하기

import sys
import webbrowser

import bs4
import requests

print("Googling...")
res = requests.get(
    "https://google.com/search?q="
    "https://pypi.org/search/?q=" + " ".join(sys.argv[1:])
)
res.raise_for_status()

# Retrive top search result links.
soup = bs4.BeautifulSoup(res.text, "html.parser")

# Open a browser tab for each result.
linkElems = soup.select(".package-snippet")
print(linkElems)
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    urlToOpen = "https://pypi.org" + linkElems[i].get("href")
    print("Opening", urlToOpen)
    webbrowser.open(urlToOpen)
