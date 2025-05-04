import requests

import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_weather(lat, lon):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        return None
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        return {
            "temp": data["main"]["temp"],
            "condition": data["weather"][0]["main"],
            "desc": data["weather"][0]["description"]
        }
    return None
