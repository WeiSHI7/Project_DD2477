import requests
from bs4 import BeautifulSoup
import pandas as pd

data_file = 
URL = "https://www.goodreads.com/book/show/2657.To_Kill_a_Mockingbird"

page = requests.get(URL)


def scrape_page(url):

    information = dict()

    if (page.status_code == 200) :

        soup = BeautifulSoup(page.content, "html.parser")

        # Gets the specific information for the book
        bookid = soup.find(id="book_id")["value"]

        title = soup.find(id="bookTitle").text.strip()

        author = soup.find('a', class_='authorName').text

        series = soup.find(id = "bookSeries").text.strip()

        ratings = soup.find("meta", itemprop="ratingCount")["content"]

        reviews = soup.find("meta", itemprop="reviewCount")["content"]

        rating = soup.find("span", itemprop="ratingValue").text.strip()

        description = soup.find(id="descriptionContainer").text.strip()[:-7]

        genres = soup.find_all('a', class_="actionLinkLite bookPageGenreLink")

        genres = set([elem.text for elem in genres])
        genres = list(genres)

        information["soup"] = soup
        information["bookid"] = bookid
        information["title"] = title
        information["author"] = author
        information["series"] = series
        information["ratings"] = ratings
        information["reviews"] = reviews
        information["rating"] = rating
        information["description"] = description
        information["genres"] = genres

    else:

        print(URL)
        print(page.status_code)

    return information



if __name__ ==  __main__:

    with 

    for url in urls:
        information = scrape_page(url)


