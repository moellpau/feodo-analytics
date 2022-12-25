import json
from datetime import datetime
import lib



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
            results.append(lib.entryFormatting(index, entry))
            index +=1


with open("old_data/all_old_data.json", "w") as json_file:
    json.dump(results, fp=json_file)