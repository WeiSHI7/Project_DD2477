import json
from Scraper import scrape_page

def write_data(filepath, urls):
    with open(filepath, "a") as file:
        info_records = dict()
        for url in urls:
            information = scrape_page(url)
            bookid = information["bookid"]
            info_records[bookid] = information
            print(type(info_records))

        file.write(json.dumps(info_records))   



if __name__ == "__main__":

    data_file = "books_information.json"
    urls = ["https://www.goodreads.com/book/show/2657.To_Kill_a_Mockingbird"]

    write_data(data_file, urls)
    # for url in urls:
    #     information = scrape_page(url)