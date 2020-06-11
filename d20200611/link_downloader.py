# 웹페이지의 URL이 주어지면 그 페이지에 링크된 모든 페이지를 다운로드 하는 프로그램 작성
# 404 상태코드를 돌려주는 모든 페이지를 표시하고 깨진 링크로 출력
import os

import bs4
import requests

url = "https://github.com/TryOC-1/dev-study"

res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "html.parser")

links = soup.select("span .js-navigation-open")

prefix_url = "https://github.com"

for link in links:
    urls = prefix_url + link.get("href")

    response = requests.get(urls)
    response.raise_for_status()

    basename = os.path.basename(urls)

    file_ext = os.path.splitext(basename)
    file_name = file_ext[0] + ".html"

    with open(os.path.join("linker", file_name), "wb") as f:
        f.write(response.content)
