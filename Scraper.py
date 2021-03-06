import requests
from bs4 import BeautifulSoup

#URL = "https://www.goodreads.com/book/show/2657.To_Kill_a_Mockingbird"



# Takes an url for a book-page on goodreads and returns a dict with all the meta data
def scrape_page(url):

    information = dict()

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    if (soup.find(id="book_id") != None) : # success!

        # soup = BeautifulSoup(page.content, "html.parser")

        print(soup.find(id="book_id"))
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

        # Adds the retrieved information into the data structure
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

        # Something went wrong when accessing the website
        # TODO maybe fix a better error message

        print(url)
        print(page.status_code)

    return information



#if __name__ == "__main__":

#    data_file = "books_information.json"
#    urls = ["https://www.goodreads.com/book/show/2657.To_Kill_a_Mockingbird"]

#    scrape_page(URL)



