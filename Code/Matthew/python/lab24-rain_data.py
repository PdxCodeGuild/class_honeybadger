

import datetime

data = [(datetime.date(2019, 9, 11), 5), (datetime.date(2019, 9, 11), 6), (datetime.date(2019, 9, 11), 6)]


import requests
import re

response = requests.get('https://or.water.usgs.gov/non-usgs/bes/')
page = response.text
files = re.findall('\w+\.rain', page)

for i in range(len(files)):
    print(i, files[i])
file_index = int(input('Which file would you like to load?'))
print('you chose ' + files[file_index])

# response = requests.get('https://or.water.usgs.gov/non-usgs/bes/hayden_island.rain')
# print(response.text)


