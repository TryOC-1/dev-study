# XKCD 홈페이지 읽어들이기
# 해당 페이지의 만화 이미지 저장
# 이전 만화로 가는 링크를 따라가기
# 가장 첫 만화에 다다를때까지 되풀이

# requests 모듈로 페이지를 다운로드 한다.
# beautiful Soup를 사용하여 페이지에 있는 만화 이미지의 URL을 찾음
# iter_content()로 만화 이미지를 하드 드라이브에 다운로드하고 저장
# 이전 만화 링크의 URL을 찾아 되풀이

import os

import bs4
import requests

url = "https://xkcd.com"  # starting url
os.makedirs("xkcd", exist_ok=True)  # store comics in ./xkcd
while not url.endswith("#"):
    # Download the page.
    print("Downloading page %s..." % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "html.parser")

    # Find the URL of the comic image.
    comicElem = soup.select("#comic img")
    if comicElem == []:
        print("Could not find comic image.")
    else:
        comicUrl = "https:" + comicElem[0].get("src")
        # Download the image.
        print("Downloading image %s..." % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()

        # Save the image to ./xkcd.
        imageFile = open(os.path.join("xkcd", os.path.basename(comicUrl)), "wb")
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = "https://xkcd.com" + prevLink.get("href")

print("Done")
