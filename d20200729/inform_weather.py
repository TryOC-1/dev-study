import json
import os
import smtplib
import sys
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
PASSWORD_KEY = os.getenv("PASSWORD_KEY")

LOCATION = {"seoul": {"lat": "37.532600", "lon": "127.024612",}}

email = "bokyoung3659@naver.com"

smtp_obj = smtplib.SMTP("smtp.gmail.com", 587)
smtp_obj.ehlo()
smtp_obj.starttls()
smtp_obj.login("bokyeong3659@gmail.com", PASSWORD_KEY)

# 커맨드 라인 입력 (현재 seoul 만 가능)
if len(sys.argv) != 2:
    print(f"Usage: {__file__} city_name")
    sys.exit(1)

location = LOCATION[sys.argv[1].lower()]

# Download the JSON data from OpenWeatherMap.org's API
url = "https://api.openweathermap.org/data/2.5/onecall"
resp = requests.get(
    url, params={"lat": location["lat"], "lon": location["lon"], "appid": API_KEY}
)
resp.raise_for_status()

weatherData = json.loads(resp.text)
daily_data = weatherData["daily"]
for day in daily_data:
    weather = day.get("weather")[0]
    day_str = datetime.utcfromtimestamp(int(day["dt"]))
    weather_status = weather.get("main")
    rain_state = day.get("rain")
    if weather_status == "Rain":
        body = f"""{day_str} -> \033[93m{weather_status}\033[0m \n
        {day_str.date()} : {rain_state}mm of {location} ."""
        send_email = smtp_obj.sendmail("bokyeong3659@gmail.com", email, body)
    elif weather_status == "Clouds":
        print(f"{day_str} -> \033[36m{weather_status}\033[0m")
    else:
        print(f"{day_str} -> \033[34m{weather_status}\033[0m")
