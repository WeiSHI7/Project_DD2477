import json

from elasticsearch import Elasticsearch, helpers


import json
import os


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


filepath = "data/json_files_final/books_information_failed_1.json"

es = Elasticsearch(scheme="http", timeout=150)

with open(filepath, "r") as filejson:
    nodes = json.load(filejson)


    # for node in nodes:
    #     _id = node['bookid']
    #     es.index(index='books',doc_type='external',id=_id,body=node)

dirpath = "data/json_files_final"

# nodes = merge_json_files(dirpath)

actions = [
{
"_index" : "books_goodreads",
"_type" : "book",
"_id" : node['bookid'],
"_source" : node
}
for node in nodes.values()
]

helpers.bulk(es,actions)