import json
from datetime import datetime

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

file_names = [
    "feodotracker-02-01-2022.json",
    "feodotracker-03-01-2022.json",
    "feodotracker-04-01-2022.json",
    "feodotracker-05-01-2022.json",
    "feodotracker-06-01-2022.json",
    "feodotracker-07-01-2022.json",
    "feodotracker-08-01-2022.json",
    "feodotracker-09-01-2022.json",
    "feodotracker-10-01-2022.json",
]

results = []
index = 0

for file in file_names:
    with open("old_data/"+file, "r") as json_file:
        data = json.load(json_file)
        
        for entry in data:
            date = cleanDate(entry["last_online"]).isoformat()[:10]
           
            results.append(
                {
                    "id": "{}_{}_{}_{}".format(index, date, entry["as_number"], entry["ip_address"]),
                    "ip_address": entry["ip_address"],
                    "as_number": entry["as_number"],
                    "as_name": entry["as_name"],
                    "country": entry["country"],
                    "date": date,
                }
            )
            index +=1


with open("old_data/all_old_data.json", "w") as json_file:
    json.dump(results, fp=json_file)