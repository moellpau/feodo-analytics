#Importing packages
import pandas as pd

#Call AWS DynamoDB to get all feodo data - execute once and then use cache
# df = pd.read_json("https://j6a7cppundv7t2fsdwke3tpkiu0qwyoo.lambda-url.eu-central-1.on.aws/")
# df.to_json("cache.json")
df = pd.read_json("cache.json")
pd.DataFrame(df)

#Create list for dates with dates_old and dates_new
dates_old = ["2022-01-02", 
        "2022-01-03", 
        "2022-01-04", 
        "2022-01-05", 
        "2022-01-06", 
        "2022-01-07", 
        "2022-01-08", 
        "2022-01-09", 
        "2022-01-10"]

dates_new = ["2022-12-21", 
        "2022-12-22", 
        "2022-12-23", 
        "2022-12-24",
        "2022-12-25"]

#Combine list
dates = dates_old + dates_new

#Define result dataframe
results = pd.DataFrame(columns=['date','total_ips', 'total_server', 'total_server_changed', 'total_ips_changed', 'percent_changed_ips'])

#Loop through each date
for date in dates:
    #Create date_df    
    date_df = df[df['date']==date]

    #Unique values for ips and server    
    total_ips = date_df['ip_address'].nunique()
    total_server = date_df['as_name'].nunique()

    #Create server_ips_df by grouping server(as name) and ip_address as unique   
    server_ips_df = pd.DataFrame(date_df.groupby("as_name")["ip_address"].nunique())
    
    #Select entries with more then one IP
    server_ips_df = server_ips_df[server_ips_df['ip_address']>1]

    #Calculate total_server_changed     
    total_server_changed = server_ips_df[server_ips_df.columns[0]].count()

    #Calculate total ips changed
    total_ips_changed = server_ips_df['ip_address'].sum()

    #Calculate percentage of changed ips
    percent_changed_ips = round(((total_ips_changed / total_ips) *100),2)

    #Fill dataframe with values    
    results.loc[len(results.index)] = [date, total_ips, total_server, total_server_changed, total_ips_changed, percent_changed_ips]

#Create region_results for January to create wordcloud with country codes
jan_df = df[df['date'].isin(dates_old)]
region_results_jan = pd.DataFrame(jan_df.groupby("country")["as_name"].count())
print(region_results_jan)

#Create region_results for December to create wordcloud with country codes
dec_df = df[df['date'].isin(dates_new)]
region_results_dec = pd.DataFrame(dec_df.groupby("country")["as_name"].count())
print(region_results_dec)

#Export dataframes as csv's'
results.to_csv("exported_dataframes/results_ip_server.csv")
jan_df.to_csv("exported_dataframes/country_codes_jan.csv")
dec_df.to_csv("exported_dataframes/country_codes_dec.csv")