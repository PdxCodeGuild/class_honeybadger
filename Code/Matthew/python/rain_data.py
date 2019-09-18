


import requests
import re
import datetime as d
import math

def load_data(url):
    
    response = requests.get(url)
    #print(response.__dict__)
    response = response.text
    new_response = re.findall('(\d\d-\w{3}-\d{4})\s+(\d+)',response)
    #print(new_response)
    ourlist = []

    for i in range(len(new_response)):
        date = new_response[i][0]
        rain = new_response[i][1]
        rain = int(rain)*.01 #converts tips to inches
        #print(date, rain)
        
        date2 = d.datetime.strptime(date, '%d-%b-%Y')
        
        ourlist.append({'year': date2.year, 'month': date2.month, 'day': date2.day, 'rain': rain})
    return ourlist


def find_average(data):
    total_days = 0
    total_rain = 0
    for i in range(len(data)):
        rain = data[i]['rain']
        total_rain += rain
        total_days +=1
    return total_rain/total_days


def find_standard_deviation(data, average):
    total_days = 0
    total_variance = 0
    for i in range(len(data)):
        rain = data[i]['rain']
        v = (rain - average)**2
        total_variance += v
        total_days += 1
    # return math.sqrt(total_variance/total_days)
    return (total_variance/total_days)**0.5
    



data = load_data('https://or.water.usgs.gov/non-usgs/bes/hayden_island.rain')    
#print(data)
average = find_average(data)
standard_deviation = find_standard_deviation(data, average)
print(f'{len(data)} records')
print(f'Average: {average}')
print(f'Standard deviation: {standard_deviation}')
print(f'68% of the data will fall within {average-standard_deviation} - {average+standard_deviation}')


# data = [{
#     'date': d.datetime(2018, 8, 11),
#     'rain': 56
# },{
#     'date': d.datetime(2018, 8, 12),
#     'rain': 23
# }]
# 
# 
# data = [{
#     'year': 2018,
#     'month': 8,
#     'day': 11,
#     'rain': 56
# },{
#     'year': 2018,
#     'month': 8,
#     'day': 12,
#     'rain': 23
# }]






    


