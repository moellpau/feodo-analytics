from datetime import datetime
import boto3

def cleanDate(input):
    try:
        date_object = datetime.strptime(input, "%Y-%m-%d")
        return date_object
    except:
        try:
            date_object = datetime.strptime(input, "%Y.%m.%d")
            return date_object
        except:
            try:
                date_object = datetime.strptime(input, "%d.%m.%Y")
                return date_object
            except:
                print("unknow format")


def entryFormatting(index, entry):
    date = cleanDate(entry["last_online"]).isoformat()[:10]
           
    return {
        "id": "{}_{}_{}_{}".format(index, date, entry["as_number"], entry["ip_address"]),
        "ip_address": entry["ip_address"],
        "as_number": entry["as_number"],
        "as_name": entry["as_name"],
        "country": entry["country"],
        "date": date,
    }


def uploadToDynamoDB(data):
    client = boto3.resource('dynamodb')
    table = client.Table("feodo_collection")

    with table.batch_writer() as batch:
        for idx, entry in enumerate(data):
            print("{}%".format(int(idx/len(data)*100)))
            batch.put_item(Item=entry)
    print("Ready")