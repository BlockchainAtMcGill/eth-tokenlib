import requests
import json
import csv
import os


call_time = '1483246800000' #00:00:00 at 01/01/2017 in millisecond epoch
call_end = '1483250400000'


coincap_url = 'http://api.coincap.io/v2/candles'
coincap_params = {
'exchange':'bitstamp',
'interval':'m1',
'baseId':'bitcoin', # Pair is reversed, meaning that base pair USD means quoteId instead and vice versa
'quoteId':'united-states-dollar',
'start': call_time,
'end': call_end

}

nomics_url = ''

# API Key is saved as environment variable
# On Powershell its $env:VarName = "value"
nomics_key = os.environ.get('nomics') 
nomics_params = {}

coincap_data = requests.get(coincap_url, coincap_params)

text = coincap_data.text

jsondata = json.loads(text)
#exchanges = jsondata['data']

if __name__ == "__main__":
	print(jsondata)
	print('Done')