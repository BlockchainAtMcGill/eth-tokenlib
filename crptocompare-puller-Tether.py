import time
import datetime
import json
import requests
import csv

def waitToNextMonth():
    #Wait to next month 1st @ 00:00 am
    now = datetime.datetime.now()
    nextM = now.month + 1
    year = now.year
    if nextM == 13:
        nextM = 1
        year += 1
    
    nextM_date = datetime.datetime(year, nextM, 1, 0, 0, 0, 0)
    delta = nextM_date - datetime.datetime.now()
    time.sleep(delta.seconds)
    
limit = 7200000
curr = int(time.time()) #time when run OR change this to any wanted date
curr_check = curr
start_usdt = 1436932800 #inception date: July 15th, 2015
crypto_url = 'https://min-api.cryptocompare.com/data/histohour'
crypto_key = 'e04eef9e1f0ff47aac52a18d315ad7eb6383fca38a881d35f90fa02f1a4dba0f'
counter = 0

while curr > start_usdt :
    counter += 1 #checks for monthly limit -- if over, sleeps until the first of the next month
    if counter >= 100000: 
        waitToNextMonth()
        counter = 0
    crypto_params = {
    'key': crypto_key,
    'fsym':'USDT',
    'tsym':'USD',
    'toTs':curr,
    'limit':'2000'
    }
    crypto_data = requests.get(crypto_url, crypto_params)
    crypto_json = json.loads(crypto_data.text)
    crypto_ohlcv = crypto_json['Data']
    if __name__ == "__main__" and any(crypto_ohlcv): #only adds to csv file if there is data in the dict
        with open('crypto_usdt.csv', 'a') as csvfile:
            fieldnames = ['time','open']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, extrasaction='ignore')
            if curr is curr_check:
                writer.writeheader()
            for i in range (0,len(crypto_ohlcv)):
                writer.writerow(crypto_ohlcv[i])
        print('Completed')
    curr -= limit
print('Done')