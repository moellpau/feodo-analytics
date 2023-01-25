#Importing packages
import boto3
import json
from decimal import Decimal

#To convert dictionary entries to JSON (so that decimal object from AWS DynamoDB is understood and converted to integer)
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

#Will be executed only if py file is called directly (not if it is included only as lib)
if __name__ == "__main__":
    res = exportData(None, None)

    print(res)



