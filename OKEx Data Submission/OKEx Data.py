
# coding: utf-8

# In[37]:


import requests 
import json
import csv
import time

#setting standards for api request URL
urlstandard="https://www.okex.com/api/spot/v3/instruments"
beginning = "86400"

crypto = {
    "XMR-USDT" : "1397804400",
    "BTC-USDT" : "1242950400",
    "ETH-USDT" : "1438214400",
    "LTC-USDT" : "1319932800",
    "BCH-USDT" : "1501545600",
    "XRP-USDT" : "1515628800",
    "EOS-USDT" : "1517382000",
    "ZRX-USDT" : "1539241200",
    "XLM-USDT" : "1406790000",
}

#traversing through every currency pair available to generate OHLCV data
for key,val in crypto.items():
    #generating dynamic Public HTTP Api request for relevant currency
    url=urlstandard+"/"+key+"/"+"candles?granularity="+beginning+"&start="+val+"&end="
    
    #print(url)
    
    r = requests.get(url) 
    crypto_json = json.loads(r.text) #Possesses a list of lists 

    keys = ['Time', 'Open', 'High','Low','Close','Volume'] #Values we want to map to
    
    #We want a list of dictionaries
    
    dataDict = [dict(zip(keys, l)) for l in crypto_json] #map values in each index to the keys
    #print(dataDict)
    
    with open(key+'.csv', 'a') as csvfile:
        
        writer = csv.writer(csvfile)
        
        writer.writerow(dataDict[0].keys())  # header row

        for row in dataDict:
            writer.writerow(row.values()) #values row

    csvfile.close()


# In[5]:


#https://www.okex.com/api

