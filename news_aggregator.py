
import requests
from bs4 import BeautifulSoup
import json

urls = [
    ("CNN", "https://edition.cnn.com/world"),
    ("BBC", "https://www.bbc.com/news"),
]

headlines = []

for source, url in urls:
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")
    tags = soup.find_all("h3")
    for tag in tags[:5]:
        headlines.append({"source": source, "headline": tag.get_text(strip=True)})

with open("headlines.json", "w", encoding="utf-8") as f:
    json.dump(headlines, f, indent=2)
