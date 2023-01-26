#Importing packages
import requests
import lib

#Function to get feodo tracker data, format this data and upload it to DynamoDB
def queryFeodo(event, context):
    x = requests.get('https://feodotracker.abuse.ch/downloads/ipblocklist_recommended.json#')

    data = x.json()
    
    results = []
    index = 0
    for entry in data:
        results.append(lib.entryFormatting(index, entry))
        index += 1
    print(results)
    lib.uploadToDynamoDB(results)

#Lambda function handler
if __name__ == "__main__":
    queryFeodo()

