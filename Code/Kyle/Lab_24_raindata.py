import requests
import re
import datetime as d
import math
import datetime


load_data = requests.get('https://or.water.usgs.gov/non-usgs/bes/columbia_ips.rain')



def data_extraction():

    date = datetime.datetime.strptime('16-JUN-2000', '%d-%b-%Y')
    page = load_data.text
    data = re.findall('(\d{2}-\w{3}-\d{4})\s+(\d+)', page)
    data_table = []

    for i in range(len(data)):
        date = data[i][0]
        rain = data[i][1]
        date2 = d.datetime.strptime(date, '%d-%b-%Y')
        data_table.append({'year': date2.year, 'month': date2.month, 'day': date2.day, 'rain': rain})
    return data_table

data_extraction()
