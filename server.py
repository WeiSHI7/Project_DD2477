import os
import json
from flask import Flask, request
from flask_cors import CORS
from elasticsearch import Elasticsearch

ELASTIC_USER = os.getenv("ELASTIC_USER")
ELASTIC_PWD = os.getenv("ELASTIC_PWD")
RECOMMENDED_BOOKS_COUNT = 3

if ELASTIC_USER is None or ELASTIC_PWD is None:
    raise Exception("ELASTIC_USER or ELASTIC_PWD not set")

app = Flask(__name__)
CORS(app)

es_client = Elasticsearch(
    "https://localhost:9200",
    ca_certs="../http_ca.crt",
    basic_auth=(ELASTIC_USER, ELASTIC_PWD)
)

cached_books = {}

def save_recommendation_csv(books):
    import pandas as pd
    result = pd.DataFrame(books, columns=["title", "author", "description", "genres"])

    result.to_csv("recommendations.csv")

def create_book_from_hit(hit):
    hit_info = hit["_source"]["fields"]

    return {
        "id": hit_info['bookid'],
        "title": hit_info['title'],
        "author": hit_info['author'],
        "description": hit_info['description'].split("\n")[1].strip(),
        "genres": hit_info['genres']
    }

def search_books_by_ids(ids):
    books = []
    
    for id in filter(lambda id: id in cached_books, ids):
        print(f"Found in cache: {id}")
        books.append(cached_books[id])

    not_in_cache = list(filter(lambda id: id not in cached_books, ids))

    if len(not_in_cache) > 0:
        print(f"Not in cache: {not_in_cache}")
        search_result = es_client.search(index="books", 
            body={
                "query": {
                    "terms": {
                        "fields.bookid": not_in_cache
                    }
                }
            }
        )

        if "hits" in search_result:
            if "hits" in search_result["hits"]:
                for hit in search_result["hits"]["hits"]:
                    book = create_book_from_hit(hit)
                    books.append(book)
                    cached_books[book["id"]] = book

    return books

def search_books_by_title(title):
    books = []

    search_result = es_client.search(index="books", 
        body={
            "query": {
                "query_string": {
                    "query": title,
                    "fields": ["fields.title", "fields.author"]
                }
            }
        }
    )

    if "hits" in search_result:
        if "hits" in search_result["hits"]:
            for hit in search_result["hits"]["hits"]:
                book = create_book_from_hit(hit)
                books.append(book)
                cached_books[book["id"]] = book

    return books

def get_combined_field(books, field):
    field_words_count = {}

    for book in books:
        if field in book:
            for word in ("".join(c for c in book[field] if c.isalnum() or c == " ")).split(" "):
                word = word.lower()
                if word not in field_words_count:
                    field_words_count[word] = 1
                else:
                    field_words_count[word] += 1
    
    combined_field = ""
    for word in field_words_count.keys():
        if word != "":
            combined_field += f"{word}^{field_words_count[word]} "

    return combined_field[:-1]

@app.route("/")
def index():
    return "Hello, World!"

@app.route("/books")
def get_books():
    query = request.args.get("q")
    res = None
    books = None

    if query is not None:
        books = search_books_by_title(query)

    if books is None:
        res = es_client.search(index="books", body={"query": {"match_all": {}}})

        books = []

        if "hits" in res:
            if "hits" in res["hits"]:
                for hit in res["hits"]["hits"]:
                    book = create_book_from_hit(hit)
                    books.append(book)
                    cached_books[book["id"]] = book


    return json.dumps(books)

@app.route("/books/<id>")
def get_book(id):
    search_result = search_books_by_ids([id])

    if len(search_result) > 0:
        return json.dumps(search_result[0])
    else:
        return "Book not found", 404

@app.route("/recommendations", methods=["POST"])
def get_recommendations():
    req = request.get_json()
    read_books = search_books_by_ids(req["read_books"])

    body = {
        "size": RECOMMENDED_BOOKS_COUNT + len(read_books),
        "query": {
            "bool": {
            "should": [
                {
                    "function_score": {
                        "query": {
                            "query_string": {
                                "fields": ["fields.description"],
                                "query": get_combined_field(read_books, "description")
                            }
                        },
                        "boost": 0.8
                    }
                },
                {
                    "function_score": {
                        "query": {
                            "query_string": {
                                "fields": ["fields.genres"],
                                "query": get_combined_field(read_books, "genres")
                            }
                        },
                        "boost": 0.2
                    }
                }
            ]
            }
        }
    }

    read_ids = {}
    for book in read_books:
        read_ids[book["id"]] = True

    res = es_client.search(index="books", body=body)

    recommended_ids = []
    # recommended_books = []

    for hit in res["hits"]["hits"]:
        if hit["_id"] not in read_ids:
            recommended_ids.append(hit["_id"])
    #         recommended_books.append(create_book_from_hit(hit))
    
    # save_recommendation_csv(recommended_books)

    return json.dumps(recommended_ids)

app.run()