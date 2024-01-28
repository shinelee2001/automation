import requests
import re

url="https://n.news.naver.com/sports/basketball/article/351/0000070909"
header ={
    'User-Agent': 'Mozilla/5.0',
    'Content-Type': 'text/html; charset=utf-8'
}
res = requests.get(url, headers=header)
results = re.findall(r'[\w\.-]+@[\w\.-]+', res.text)
print(results)
results = list(set(results))
print(results)