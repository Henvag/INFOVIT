from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urljoin

url = "https://en.wikipedia.org/wiki/Star_Wars:_The_Rise_of_Skywalker"

html = urlopen(url)

soup = BeautifulSoup(html, 'html.parser')

tds = soup.find_all("td", {"class": "yes table-yes2 notheme"})

for td in tds:
    print(td.parent.get_text())


