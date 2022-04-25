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
                nodes_in = json.loads(filejson)
                nodes = nodes | nodes_in
    return nodes