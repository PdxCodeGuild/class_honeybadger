

import requests
import json

url = 'https://api.forismatic.com/api/1.0/?method=getQuote&key=457653&format=json&lang=en'
response = requests.get(url)
data = json.loads(response.text)

quote_body = data['quoteText'].strip()
quote_author = data['quoteAuthor']

print(f'"{quote_body}" - {quote_author}')
