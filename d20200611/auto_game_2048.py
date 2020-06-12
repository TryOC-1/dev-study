# 2048
# 위, 아래, 왼쪽, 오른쪽 화살표 키를 눌러 타일을 밀어 합치는 간단한 게임
# https://gabrielecirulli.github.io/2048/ 에서 게임을 열고 키 입력을 계속해서 자동으로 게임을 하는 프로그램 작성

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome("/Users/gimbogyeong/Downloads/chromedriver")
browser.get("https://gabrielecirulli.github.io/2048/")
htmlElem = browser.find_element_by_tag_name("html")
path = "/html/body/div[3]/div[4]/div[1]/p"
div_elems = browser.find_element_by_class_name("game-message")
temp = div_elems.find_element_by_tag_name("p").text

while True:
    htmlElem.send_keys(Keys.RIGHT)
    htmlElem.send_keys(Keys.UP)
    htmlElem.send_keys(Keys.DOWN)
    htmlElem.send_keys(Keys.LEFT)

    game_over = htmlElem.find_elements_by_class_name("game-over")
    if game_over:
        break
