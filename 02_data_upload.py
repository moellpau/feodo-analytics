import boto3
import json

client = boto3.resource('dynamodb')

table = client.Table("feodo_collection")

print(table.table_status)

data = []

with open("old_data/all_old_data.json", "r") as json_file:
    data = json.load(json_file)

with table.batch_writer() as batch:
    for idx, entry in enumerate(data):
        print("{}%".format(int(idx/len(data)*100)))
        batch.put_item(Item=entry)

print("Ready")