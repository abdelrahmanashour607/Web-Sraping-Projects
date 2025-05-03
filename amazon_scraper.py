
import requests
from bs4 import BeautifulSoup
import csv

headers = {
    "User-Agent": "Mozilla/5.0",
}
url = "https://www.amazon.com/s?k=headphones"

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")
products = soup.find_all("div", {"data-component-type": "s-search-result"})

with open("amazon_products.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Product Name", "Price", "Rating"])
    for product in products:
        name = product.h2.text.strip()
        price = product.find("span", "a-price")
        rating = product.find("span", "a-icon-alt")
        writer.writerow([
            name,
            price.text.strip() if price else "N/A",
            rating.text.strip() if rating else "N/A"
        ])
