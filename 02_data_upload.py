#Importing packages
import json
import lib

data = []

#Open and load all_old_data json file
with open("old_data/all_old_data.json", "r") as json_file:
    data = json.load(json_file)

#Call uploadToDynamoDB function from lib to upload all_old_data to DynamoDB
lib.uploadToDynamoDB(data)