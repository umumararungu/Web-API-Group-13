#!/usr/bin/python3
"""
searching movie from api source
"""

import requests

url = "https://unogsng.p.rapidapi.com/genres"

headers = {
	"X-RapidAPI-Key": "22dfb032bcmshd468812fcf0f1d1p145ebfjsna08d82b4d26f",
	"X-RapidAPI-Host": "unogsng.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())