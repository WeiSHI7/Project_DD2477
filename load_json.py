import json

from elasticsearch import Elasticsearch, helpers


import json
import os

ELASTIC_USER = os.getenv("ELASTIC_USER")
ELASTIC_PWD = os.getenv("ELASTIC_PWD")

if ELASTIC_USER is None or ELASTIC_PWD is None:
    raise Exception("ELASTIC_USER or ELASTIC_PWD not set")


def merge_json_files(dirpath):
    directory = os.fsencode(dirpath)
    nodes = {}
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".json"):
            filename = dirpath + "/" + filename
            with open(filename, "r") as filejson:
                nodes_in = json.load(filejson)
                nodes = dict(nodes,**nodes_in)
    return nodes

client = Elasticsearch(
    "https://localhost:9200",
    ca_certs="../http_ca.crt",
    basic_auth=(ELASTIC_USER, ELASTIC_PWD)
)

doc_count = 0

for i in range(1, 11):
    filepath = f"data/json_files_final/books_information_{i}.json"

    with open(filepath, "r") as filejson:
        nodes = json.load(filejson)

    for k in nodes.keys():
        nodes[k]["genres"] = ", ".join(nodes[k]["genres"])

    body = []

    for node in nodes.values():
        body.append({"index": {"_index": "books", "_id": node["bookid"]}})
        body.append({"fields": node})

    res = client.bulk(body=body)

    doc_count += len(nodes)

    print(f"Indexed {doc_count} documents")