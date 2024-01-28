import requests
from bs4 import BeautifulSoup

url = "http://boannews.com"
res = requests.get(url).text
soup = BeautifulSoup(res, "lxml")

print("Links:")
for link in soup.find_all("a"):
    link_href = str(link['href'])
    if (link_href.startswith('http')):
        print(link_href)
    elif (link_href == None):
        continue
    else:
        print(url + link_href)