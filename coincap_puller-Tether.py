import requests
import json
import time

start = 1491019200000
response = []
counter = 0
while start < int(time.time()*1000):
  if counter > 80:
      time.sleep(15)
      counter = 0
  response.append((requests.get("https://api.coincap.io/v2/assets/tether/history?interval=m1&start="+ str(start) + "&end="+ str(start+86340000))))
  start += 86400000
  counter += 1
  

k=0
stringJSON = []
while k <= (len(response)-1):
  with open("coincap-minutelyT"+ str(k) + "-24hrs.json", "w") as outfile:
    stringJSON.append(json.loads(response[k].content))
    json.dump(stringJSON[k], outfile, sort_keys = True, indent = 4, ensure_ascii = False)
    k+=1
    
import csv
import json

t=0
d = []
while t <= (len(response)-1):
  f1 = open("coincap-minutelyT"+ str(t) + "-24hrs.json")
  d.append(json.load(f1))
  f1.close
  t+=1

csvfile = open('Tether-usd-18-03-2019.csv', 'w')

fieldnames = ['time', 'priceUsd'];

writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

writer.writeheader()

r=0
while r <= (len(d)-1):
  for entry in d[r]['data']:
    writer.writerow({'time': entry['time'], 'priceUsd': entry['priceUsd']})
  r+=1
    
csvfile.close
