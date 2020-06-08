import sys
import webbrowser

import pyperclip

# 명령행 매개변수 또는 클립보드에서 주소가져오기
# 주소에 대한 구글 지도 페이지를 웹브라우저에서 열기
# sys.argv로부터 명령행 매개변수 읽기
# 클립보드 내용 읽어오기
# 웹 브라우저를 열기 위해 webbrrowser.open() 함수 호출

# Lanches a map in the browser using an address from the command line or clipboard

if len(sys.argv) > 1:
    # Get address from command line.
    address = " ".join(sys.argv[1:])
else:
    # Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open("https://www.google.com/maps/place/" + address)
