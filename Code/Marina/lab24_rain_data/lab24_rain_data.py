
import requests
import re
import datetime


response = requests.get('https://or.water.usgs.gov/non-usgs/bes/shipyard.rain')

text = response.text
date = datetime.datetime.strptime('22-FEB-2012', '%d-%b-%Y')
# print(date.month)
# print(date.day)
data = re.findall('(\d{2}-\w{3}-\d{4})\s+(\d+)', text)

for i in range(len(data)):
    row = data[i]
    date_str = row[0]
    daily_total = int(row[1])
    date = datetime.datetime.strptime(date_str, '%d-%b-%Y')
    # print(date_str)
    # print(daily_total)
    # print(data)

    date_str = date.strftime('%d/%m/%Y')
    # print(f' the rainfall for {date_str} was {daily_total}')
    # print(f' the rainfall for {date.year} in the month of {date.month} was {daily_total}')

    # data[i] = (date, daily_total)
    data[i] = {
        'year': date.year,
        'month': date.month,
        'day': date.day,
        'daily_total': daily_total
    }


for row in data:
    if row['year'] == year:
        print(f"The daily total of {row['month']}/{row['day']} is {row['daily_total']}")

    data_year = [row for row in data if row['year'] == year]
    total = 0
    for row in data_year:
        total += row['daily_total']

# yearly_total = 0
#             # if row['year'] == 2017:
# for k, v in data[i].items():
#     print("{{{0}: {1}}}".format(k, sum(v)))
    # print(yearly_total)
            # print(f"The average rain fall for year {row['year']} is {row['daily_total']})
        # average_rain(yearly_total)
