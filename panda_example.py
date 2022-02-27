## pandas example
import json
import pandas as pd

#open file
with open('switches.json') as file_pandas:
    df = pd.read_json(file_pandas)
    
#drop unneccessary columns
df = df.drop(['tags', 'id', 'use_dns', 'comment', 'active', 'start_downtime', 'end_downtime'], 1)

#publish csv
df.to_csv('panda_switches.csv', index=False)
