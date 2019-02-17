import requests
import json
import csv
import os

hours_ms = 86400000
num_call = 1483246800000


# Some sample time values
call_time = '1483246800000' #00:00:00 at 01/01/2017 in millisecond epoch
call_end = '1483250400000'

end = num_call + hours_ms

coincap_url = 'http://api.coincap.io/v2/candles'
coincap_params = {
'exchange':'bitfinex',
'interval':'m1',
'baseId':'bitcoin', # Pair is reversed, meaning that base pair USD means quoteId instead and vice versa
'quoteId':'united-states-dollar'
,'start': num_call,
'end': end
}

nomics_url = 'https://api.nomics.com/v1/exchange_candles'

# API Key is saved as environment variable
# On Powershell(Windows) its $env:VarName = "value"
nomics_key = os.environ.get('nomics') 
nomics_params = {
'key': nomics_key,
'interval':'1m',
'exchange':'binance',
'market':'BTCUSDT'
# ,'start':'',
# 'end':''
}

coincap_data = requests.get(coincap_url, coincap_params)
# nomics_data = requests.get(nomics_url, nomics_params)

coincap_json = json.loads(coincap_data.text)
coincap_ohlcv = coincap_json['data']
if __name__ == "__main__":
	with open('coincap_ex.csv', 'w') as csvfile:
		fieldnames = coincap_ohlcv[0].keys()
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		for i in range (0,len(coincap_ohlcv)):
			writer.writerow(coincap_ohlcv[i])
	
	
	print('Completed')
	