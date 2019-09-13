



import requests
import json

response = requests.get('http://madlibz.herokuapp.com/api/random')
data = json.loads(response.text)

title = data['title']
blanks = data['blanks']
values = data['value']

print(title)

text = ''
for i in range(len(blanks)):
    user_input = input('Give me a ' + blanks[i] + ': ')
    text += values[i] + user_input

print(text)