import requests
from bs4 import BeautifulSoup
import pandas as pd

# The partial url for the pages that should be scraped,
# the final page number is added in each iteration
URL = "https://www.goodreads.com/list/show/264.Books_That_Everyone_Should_Read_At_Least_Once?page="

url_file = "data/urls.txt"


# Gets all urls to the books in the list
# Returns these urls in a list
def scrape_urls(url):

    page = requests.get(url)

    urls = []

    if (page.status_code == 200) : # success!

        soup = BeautifulSoup(page.content, "html.parser")
        
        urls = soup.find_all('a', class_="bookTitle")

        urls = [elem["href"] for elem in urls]

    else:
        
        # something went wrong with accessing the website
        # TODO maybe fix a better error message

        print(URL)
        print(page.status_code)

    return urls



def main():
    

    with open(url_file, 'w') as outfile:

        for page in range (1, 101):

            # The current page to be scraped
            url = URL + str(page)
            
            # The urls found on that page
            urls = scrape_urls(url)

            for new_url in urls:
                
                outfile.write(new_url)
                outfile.write('\n')

            print(f"Scraped page {page}")

if __name__ ==  "__main__":

    main()


