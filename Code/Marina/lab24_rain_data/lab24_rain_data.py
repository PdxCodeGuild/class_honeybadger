
import requests
import re
import datetime

response = requests.get('https://or.water.usgs.gov/non-usgs/bes/shipyard.rain')

text = response.text
date = datetime.datetime.strptime('22-FEB-2012', '%d-%b-%Y')
# print(date.month)
# print(date.day)
data = re.findall('(\d{2}-\w{3}-\d{4})\s+(\d+)', text)

for row in data:
    date_str = row[0]
    daily_total = int(row[1])

    print(date_str)
    print(daily_total)
    print()




# print(f' on the {date.day}nd of {date.month}nd month of {date.year} {files}')

# print(date)
# print(date.strftime('%d-%b-%Y'))
# print(text)
