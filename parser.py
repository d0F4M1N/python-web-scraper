import requests
from config import HEADERS
from bs4 import BeautifulSoup
from utils import clean_price, rating_to_int
import time
from config import DELAY

BASE_URL = "https://books.toscrape.com/catalogue/"


def parse_all_pages(start_url: str, max_pages: int = 3):
    all_products = []
    current_url = start_url

    for i in range(max_pages):
        print(f"Parsing page {i+1}: {current_url}")

        html = get_html(current_url)
        if not html:
            break

        products = parse_page(html)
        all_products.extend(products)

        current_url = get_next_page_url(current_url)
        time.sleep(DELAY)

    return all_products


def get_next_page_url(current_url: str) -> str | None:
    if "page-" in current_url:
        base, page = current_url.rsplit("page-", 1)
        next_page = int(page.replace(".html", "")) + 1
        return f"{base}page-{next_page}.html"
    else:
        return current_url.replace("index.html", "page-2.html")


def parse_page(html: str) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")

    products = []

    items = soup.find_all("article", class_="product_pod")

    for item in items:
        # название
        name = item.h3.a["title"]

        # цена
        price = clean_price(item.find("p", class_="price_color").text)

        rating_class = item.find("p", class_="star-rating")["class"]
        rating = rating_to_int(rating_class[1])

        # ссылка
        relative_url = item.h3.a["href"]
        url = BASE_URL + relative_url

        products.append({
            "name": name,
            "price": price,
            "rating": rating,
            "url": url
        })

    return products


def get_html(url: str) -> str:
    response = requests.get(url, headers=HEADERS)
    response.encoding = "utf-8"
    if response.status_code == 200:
        return response.text
    else:
        print(f"Error: {response.status_code}")
        return ""
