import requests
import json
from dotenv import load_dotenv
import os
import urllib.parse
from pprint import pprint

load_dotenv()
api_key = os.getenv('API_KEY')
cx = os.getenv('CX')

query = 'mosque near me'
url = url = "https://www.googleapis.com/customsearch/v1"
params = {
    "key": api_key,
    "cx" : cx,
    "q" : query
}

response = requests.get(url, params=params)
data = response.json()

with open("results.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
pprint(data)