#Importing packages
import pandas as pd
import numpy as np

#Call AWS DynamoDB to get all feodo data - execute once and then use cache
# df = pd.read_json("https://j6a7cppundv7t2fsdwke3tpkiu0qwyoo.lambda-url.eu-central-1.on.aws/")
# df.to_json("cache.json")
df = pd.read_json("cache.json")
pd.DataFrame(df)

#Create months list for January and December dates
months = [
        ["2022-01-02", 
        "2022-01-03", 
        "2022-01-04", 
        "2022-01-05", 
        "2022-01-06", 
        "2022-01-07", 
        "2022-01-08", 
        "2022-01-09", 
        "2022-01-10"],
        ["2022-12-21", 
        "2022-12-22", 
        "2022-12-23", 
        "2022-12-24",
        "2022-12-25"]
]

results = []

#Loop over month
for month in months:

        #Define month_result dataframe
        month_result = pd.DataFrame(columns=['date','total_previous_ips', 'total_current_ips', 'total_growth_percentage', 'same_ips', 'new_ips', 'portion_new_ips'])

        #Loop thorugh each entry in month list
        for i in range(1,len(month)):

                #Get current and previous date from month list
                date_current = month[i]
                date_previous = month[i-1]

                #Create dataframe with current and previous dates
                day_previous = df[df['date']==date_previous]
                day_current = df[df['date']==date_current]

                #Format day_previous dataframe
                day_previous = day_previous.drop(columns=['date','as_name', 'id', 'country', 'as_number'])
                day_previous = pd.unique(day_previous['ip_address'])
                day_previous = pd.DataFrame(day_previous)

                #Format day_current dataframe
                day_current = day_current.drop(columns=['date','as_name', 'id', 'country', 'as_number'])
                day_current = pd.unique(day_current['ip_address'])
                day_current = pd.DataFrame(day_current)

                #Calculate same_ips with merging day_current and day_previous dataframe
                same_ips = pd.merge(day_current, day_previous, on=0, how='inner')

                #Calculate new_ips as difference between entries in day_current and same_ips
                new_ips = len(day_current) - len(same_ips)

                #Calculate percentage of ratio of entries of day_current and day_previous dataframe
                total_growth_percentage = round(((len(day_current)/len(day_previous))-1)*100, 2)

                #Calculate portion of new ips
                portion_new_ips = round(((new_ips/len(day_current)))*100, 2)

                #Fill dataframe with values
                month_result.loc[len(month_result.index)] = [date_current, len(day_previous), len(day_current), total_growth_percentage, len(same_ips), new_ips, portion_new_ips]
        
        #Append month_result to results
        results.append(month_result)

#Export results as csv
results[0].to_csv("exported_dataframes/results_comparison_jan.csv")
results[1].to_csv("exported_dataframes/results_comparison_dec.csv")





