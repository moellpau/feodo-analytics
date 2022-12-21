import json
import lib

data = []

with open("old_data/all_old_data.json", "r") as json_file:
    data = json.load(json_file)

lib.uploadToDynamoDB(data)