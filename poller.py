import requests
import json
import csv
import os



url = 'https://jsonplaceholder.typicode.com/posts/1'
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

text = response.text

jsondata = json.loads(text)

if __name__ == "__main__":
	jsondata['title']
	
	with open('test.csv','w') as csvfile:
		fieldnames = ['title','body']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		writer.writerow({'title': jsondata['title'], 'body': jsondata['body']})
	print('Completed')
