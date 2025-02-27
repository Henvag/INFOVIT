from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urljoin

url = "https://en.wikipedia.org/wiki/Star_Wars:_The_Rise_of_Skywalker"

html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

all_links = soup.find_all("a", href=True)
all_images = soup.find_all("img", src=True)

print("\n=== LINKS ===")
for link in all_links:
    absolute_url = urljoin(url, link['href'])
    print(f"Link: {absolute_url}")

print("\n=== IMAGES ===")
for image in all_images:
    absolute_url = urljoin(url, image['src'])
    print(f"Image: {absolute_url}")