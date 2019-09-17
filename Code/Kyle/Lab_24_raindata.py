import requests
import re
import datetime
import math




data_table = requests.get('https://or.water.usgs.gov/non-usgs/bes/columbia_ips.rain')


date = datetime.datetime.strptime('16-JUN-2000', '%d-%b-%Y')
page = data_table.text
data = re.findall('(\d{2}-\w{3}-\d{4})\s+(\d+)', page)
# print(data_table)

for row in data:
    # row = data[i]
    date = datetime.datetime.strptime(row[0], '%d-%b-%Y')
    daily_total = int(row[1])
    #convert = datetime.datetime.strptime('date', '%d-%b-%Y')
    print(date.year, date.month, date.day, daily_total)

    sum = 0
    for num in row[1]:
        sum = sum + daily_total

    print(f'the sum is', sum)
