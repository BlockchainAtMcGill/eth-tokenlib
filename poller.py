import requests
import json
url = 'https://jsonplaceholder.typicode.com/posts/1'
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

text = response.text

jsondata = json.loads(text)

if __name__ == "__main__":
	jsondata['title']
	print('Title data is', jsondata['title'])



