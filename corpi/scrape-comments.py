import requests
import json
import string

body = requests.get('https://www.reddit.com/r/ethtrader/comments.json?limit=1000', headers = {'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.85 Safari/537.36'}).json()

printable = set(string.printable)

with open('ico_text/ethtrader.txt', 'a') as f:
    for item in body['data']['children']:
        data = item['data']
        if 'body' in data and data['body']:
            f.write(''.join(filter(lambda x: x in printable, data['body'])))
