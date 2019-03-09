import requests
import csv
import json
import datetime
import pandas as pd
import time 

i = 0

filename = "capcoin-btc-usd-2014-2019.csv"  
with open(filename, "w") as csvfile:

    for year in range(2014,2020):
    
    
        # open the csv file for output and write the header information
        fieldnames = ['date', 'priceUsd'];
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
    
        # setup the range of dates for the given year
        dt_range = pd.date_range(str(year)+'-01-01',freq='D',periods=365)
    
        # iterate through the date range; call coincap.io and get a daily response file
        # write the daily respone file to the csv
    
        for dt in dt_range:
           
            currentDay = str(dt)
            d = time.mktime(datetime.datetime.strptime(currentDay, "%Y-%m-%d %H:%M:%S").timetuple()) * 1000
            epoch1 = d   # this is epoch or unix time (I experimented not sure what the difference is between UTC and UNIX, but this is UNIX time )
                       
            # this is epoch end time
            epoch2 = d + 86400000 #go to the next day
        
            url = "https://api.coincap.io/v2/assets/bitcoin/history?interval=m1"+"&start="+str(epoch1)+"&end="+str(epoch2)
        
            response = requests.get(url)
            #print(response)
            #stringJSON2 = json.loads(response.content)

            if (response):
                stringJSON = json.loads(response.content)
                
                for entry in stringJSON['data']:
                    writer.writerow({'date': entry['date'], 'priceUsd': entry['priceUsd']})                  

                    
