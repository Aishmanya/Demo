import csv
import json
f1= open("trial.csv", 'r')
f2=open("trialJ.json", 'w')
f_data=csv.reader(f1)
data={}
for row in f_data:
    key,value=row
    data[key]=value
json.dump(data, f2, indent=4)
f1.close()
f2.close()