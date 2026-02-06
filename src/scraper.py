import requests
from notifier import notify_discord
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from storage import load_books, save_books
from compare import find_new_books

BASE_URL = "https://books.toscrape.com"

def get_books(max_books=None):
    print("startar..")
    books = []
    page_url = BASE_URL

    while page_url:
        print(f"laddar..: {page_url}")
        response = requests.get(
            page_url,
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=10
        )
        response.raise_for_status()


        soup = BeautifulSoup(response.text, "html.parser")
    

        for book in soup.select("article.product_pod"):
            title = book.h3.a["title"]
            price = book.select_one("p.price_color").text.strip()
            relative_url = book.h3.a["href"]
            url = urljoin(page_url, relative_url)

            books.append({
                "id": title,
                "title": title,
                "price": price,
                "url": url
            })

            if max_books and len(books) >= max_books:
                return books
            
        next_button = soup.select_one("li.next a")
        if next_button:
            page_url = urljoin(page_url, next_button["href"])

        else:
            page_url = None

    return books

if __name__ == "__main__":
    new_books = get_books(max_books=50)

    old_books = load_books()

    added = find_new_books(old_books, new_books)

    if added:
        notify_discord(added)

    if added:
        print(f"{len(added)} new books found:")
        for b in added:
            print(f'+{b["title"]} - {b["price"]}')

    else:
        print("no new books")

    save_books(new_books)


    for b in new_books:
        print(f'{b["title"]} - {b["price"]}')