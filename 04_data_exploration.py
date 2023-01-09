import pandas as pd

#df = pd.read_csv(r'DynamoDB_results.csv') 
df = pd.read_json("https://j6a7cppundv7t2fsdwke3tpkiu0qwyoo.lambda-url.eu-central-1.on.aws/")
pd.DataFrame(df)

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

dates = dates_old + dates_new
results = pd.DataFrame(columns=['date','total_ips', 'total_server', 'total_server_changed', 'total_ips_changed', 'percent_changed_ips'])

for date in dates:
    date_df = df[df['date']==date]

    total_ips = date_df['ip_address'].nunique()
    total_server = date_df['as_name'].nunique()

    server_ips_df = pd.DataFrame(date_df.groupby("as_name")["ip_address"].nunique())
    server_ips_df = server_ips_df[server_ips_df['ip_address']>1]

    total_server_changed = server_ips_df[server_ips_df.columns[0]].count()
    total_ips_changed = server_ips_df['ip_address'].sum()
    percent_changed_ips = round(((total_ips_changed / total_ips) *100),2)

    results.loc[len(results.index)] = [date, total_ips, total_server, total_server_changed, total_ips_changed, percent_changed_ips]

print(results)

jan_df = df[df['date'].isin(dates_old)]
region_results_jan = pd.DataFrame(jan_df.groupby("country")["as_name"].count())
print(region_results_jan)

dec_df = df[df['date'].isin(dates_new)]
region_results_dec = pd.DataFrame(dec_df.groupby("country")["as_name"].count())
print(region_results_dec)

# Speichern der dataframes als csv's
results.to_csv("exported_dataframes/results_ip_server.csv")
jan_df.to_csv("exported_dataframes/country_codes_jan.csv")
dec_df.to_csv("exported_dataframes/country_codes_dec.csv")