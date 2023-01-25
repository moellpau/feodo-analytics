#Importing packages
import json
import lib

#Feodeotracker data from January given in task
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

#Loop over each json file
for file in file_names:
    #Open json file
    with open("old_data/"+file, "r") as json_file:
        data = json.load(json_file)
        #For each entry, append to results and apply function entryFormatting from lib
        for entry in data:
            results.append(lib.entryFormatting(index, entry))
            index +=1

#Open all_old_data file and save results in this json file
with open("old_data/all_old_data.json", "w") as json_file:
    json.dump(results, fp=json_file)