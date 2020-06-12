import os

import bs4
import requests

url = "https://imgur.com/search?q=car"
os.makedirs("imgur", exist_ok=True)
print("Downloading page %s..." % url)
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "html.parser")
images = soup.select(".image-list-link img")

for image in images:
    img_link = "https:" + image.get("src")
    print("Downloading image %s..." % (image))
    res = requests.get(img_link)
    res.raise_for_status()

    imgFile = open(os.path.join("imgur", os.path.basename(img_link)), "wb")
    for chunk in res.iter_content(100000):
        imgFile.write(chunk)
    imgFile.close()
