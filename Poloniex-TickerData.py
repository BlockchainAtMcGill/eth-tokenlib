
# coding: utf-8

# In[23]:


import requests 
import json
import csv
import time

#setting standards for api request URL
urlstandard="https://poloniex.com/public?command=returnChartData&"
maximumretrievetime="&resolution=auto"
period="300"

#dictionary which holds key as Currency Paid highlighted in Poloniex and value as inception date of currency(UNIX Timestamp)
crypto = {
    "USDC_XMR" : "1397804400",
    "USDC_BTC" : "1242950400",
    "USDC_ETH" : "1438214400",
    "USDC_LTC" : "1319932800",
    "USDC_BCH" : "1501545600",
    "USDC_XRP" : "1515628800",
    "USDC_USDT":"1407974400",
}

#traversing through every currency pair available to generate OHLCV data
for key,val in crypto.items():
    #generating dynamic Public HTTP Api request for relevant currency
    url=urlstandard+"currencyPair="+key+"&start="+val+maximumretrievetime+"&period="+period
    r = requests.get(url) 
    crypto_json = json.loads(r.text)
    with open(key+'.csv', 'a') as csvfile:
    
        writer = csv.writer(csvfile)

        writer.writerow(crypto_json[0].keys())  # header row

        for row in crypto_json:
            writer.writerow(row.values()) #values row

    csvfile.close()

