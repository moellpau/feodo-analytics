import requests
import lib


def queryFeodo():
    x = requests.get('https://feodotracker.abuse.ch/downloads/ipblocklist_recommended.json#')

    data = x.json()
    
    results = []
    index = 0
    for entry in data:
        results.append(lib.entryFormatting(index, entry))
        index += 1
    print(results)
    lib.uploadToDynamoDB(results)

if __name__ == "__main__":
    queryFeodo()

