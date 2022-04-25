import json
from elasticsearch import Elasticsearch, helpers


filepath = "data\books_information_1.json"

es = Elasticsearch([{'host':'localhost', 'port': 9200}], scheme="http")

with open(filepath, "r") as filejson:
    nodes = json.load(filejson)


    # for node in nodes:
    #     _id = node['bookid']
    #     es.index(index='books',doc_type='external',id=_id,body=node)

    actions = [
    {
    "_index" : "nodes_bulk",
    "_type" : "external",
    "_id" : str(node['index']),
    "_source" : node
    }
    for node in nodes
    ]

helpers.bulk(es,actions)