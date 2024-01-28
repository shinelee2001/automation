from bs4 import BeautifulSoup
import requests

url = "http://boannews.com"

headers = {"User-Agent": "Mozilla/5.0", "Content-Type": "text/html; charset=utf-8"}

req = requests.get(url, headers=headers)
soup = BeautifulSoup(req.text, "lxml")
tags = soup.select("#headline3 > ul > li:nth-child(1) > p")

for tag in tags:
    print(tag.string)
