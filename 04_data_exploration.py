import json
import pandas as pd

data = []

with open("old_data/all_old_data.json", "r") as json_file:
    data = json.load(json_file)

#print(data)

df = pd.DataFrame.from_dict(data, orient='columns')
#print(df)

df_02 = df[df['date']=='2022-01-02']
print(df_02)

total_ips = df_02['ip_address'].nunique()
print(total_ips)

total_server = df_02['as_name'].nunique()
print(total_server)

server_ips_df = pd.DataFrame(df_02.groupby("as_name")["ip_address"].nunique())
server_ips_df = server_ips_df[server_ips_df['ip_address']>1]
print(server_ips_df)

total_server_changed = server_ips_df[server_ips_df.columns[0]].count()
print(total_server_changed)


total_ips_changed = server_ips_df['ip_address'].sum()
print(total_ips_changed)

percent_changed_ips = total_ips_changed / total_ips *100
print(percent_changed_ips)

#alle server filtern nach, die die mehr als 1 stehen hat (Summe) - dann überall -1 rechnen und die Summe von allen IP addressen für alle Server