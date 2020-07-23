import os

import bs4
import requests

url = "https://comic.naver.com/webtoon/\
        detail.nhn?titleId=733766&no=37&weekday=mon"
os.makedirs("naver", exist_ok=True)

print(f"Download naver webtoon : {url}")
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "html.parser")

web_img = soup.select(".wt_viewer img")
if web_img is []:
    print("Not found.")
else:
    for img in web_img:
        img_url = img.get("src")
        print(f"Download image {img_url}")
        res = requests.get(img_url)

        img_file = open(os.path.join("naver", os.path.basename(img_url)), "wb")
        for check in res.iter_content(100000):
            img_file.write(check)
        img_file.close()

print("Done.")
