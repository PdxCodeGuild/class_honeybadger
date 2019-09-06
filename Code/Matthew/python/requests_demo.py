
import requests


response = requests.get('https://www.gutenberg.org/files/60236/60236-0.txt')
text = response.text
print(text)
