import json
from Scraper import scrape_page

def write_data(filepath, filepath_failed, urls):
    url_fail = []
    with open(filepath, "a") as file:
        info_records = dict()
        for url in urls:
            information = scrape_page(url)
            if "bookid" in information.keys():
                bookid = information["bookid"]
                info_records[bookid] = information
            else:
                url_fail.append(url)
                print("url failed:" + url)


        file.write(json.dumps(info_records)) 

    with open(filepath_failed, "w") as failed:
        for url in url_fail:
            failed.write(url)
            failed.write("\n")

def load_urls(filepath):
    urls = []
    with open(filepath, "r") as file:
        while True:
            line = file.readline()
            url = "https://www.goodreads.com" + line
            urls.append(url)
            if not line:
                break
    return urls    

if __name__ == "__main__":
    
    # urls_file = "data/urls.txt"
    # failed_file = "data/failed.txt"
    # data_file = "data/books_information.json"
    # urls = ["https://www.goodreads.com/book/show/2657.To_Kill_a_Mockingbird"]

    urls_file = "data/urls_test.txt"
    failed_file = "data/failed_test.txt"
    data_file = "data/books_information_test.json"

    urls = load_urls(urls_file)
    write_data(data_file, failed_file, urls)
    # for url in urls:
    #     information = scrape_page(url)