import json
import csv

## open file ##
file = open('switches.json')
switch_data = json.load(file)

data_file = open('switches.csv', 'w')

# create the csv writer object
csv_writer = csv.writer(data_file)

#write header
csv_writer.writerow(["switch", "ip"])

##rifle through switches and write each row to csv
for switch in switch_data:
    csv_writer.writerow([switch["name"], switch["ip"]])
