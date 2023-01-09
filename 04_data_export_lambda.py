import boto3
import json

from decimal import Decimal

#Um Dictionary-Einträge in JSON umzuwandeln (damit Dezimalobjekt aus AWS DynamoDB verstanden wird + in integer umgwandelt wird)
class DecimalEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, Decimal):
      return int(obj)
    return json.JSONEncoder.default(self, obj)

def downloadFromDynamoDB():
    client = boto3.resource('dynamodb')
    table = client.Table("feodo_collection")

    results = table.scan()
    return results["Items"]

def exportData(event, context):
    results = downloadFromDynamoDB()
    return {
        'statusCode': 200,
        'body': json.dumps(results, cls=DecimalEncoder)
    }

#Wird nur ausgeführt, wenn py-Datei direkt aufgerufen wird (nicht wenn sie nur als lib eingebunden wird)
if __name__ == "__main__":
    res = exportData(None, None)

    print(res)



