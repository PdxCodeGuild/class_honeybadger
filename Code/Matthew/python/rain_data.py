


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
        rain = int(rain)*.01*2.54 #converts tips to cm
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
    



def find_day_most_rain(data):
    r = data[0]
    for row in data:
        if row['rain'] > r['rain']:
            r = row
    return r
            

def find_year_most_rain(data):
    
    # years = set()
    # for row in data:
    #     years.add(row['year'])
    # years = list(years)
    # years.sort()
    
    # years = list({row['year'] for row in data})
    # years.sort()
    
    # data = data[:20]
    
    years = []
    for row in data:
        if row['year'] not in years:
            years.append(row['year'])
    years.sort()
    # print(years)
    
    
    #           0     1    2    ...
    # years  = [1999, 2000, 2001, ...]
    # totals = [   0,    0,    0, ...]
    # counts = [   0,    0,    0, ...]
    
    # totals = []
    # counts = []
    # for year in years:
    #     totals.append(0)
    #     counts.append(0)
    # 
    # totals = [0 for year in years]
    # counts = [0 for year in years]
    
    totals = [0]*len(years)
    counts = [0]*len(years)
    
    for row in data:
        
        year_index = years.index(row['year'])
        totals[year_index] += row['rain']
        counts[year_index] += 1
        
        # print(f'row is {row}')
        # print(years)
        # print(totals)
        # print(counts)
        # print()
    
    year_averages = []
    for year in years:
        data_year = [row for row in data if row['year'] == year]
        # print(data_year)
        # print(f'Year {year} has {len(data_year)} records')
        average = find_average(data_year)
        # print(f'The average rainfall for {year} is {average}cm')
        year_averages.append((year, average))
    
    # max_year = year_averages[0]
    # for year_average in year_averages:
    #     if year_average[1] > max_year[1]:
    #         max_year = year_average
    
    
    
    return max(year_averages, key=lambda x: x[1])
    
    
    
    


# def add(a, b=1):
#     return a + b
# add = lambda a, b: a + b
# add(5, 2)
# add(5)
# add(5, b=2)
        
        
    
        
        
    
    
    


data = load_data('https://or.water.usgs.gov/non-usgs/bes/hayden_island.rain')    
#print(data)
average = find_average(data)
standard_deviation = find_standard_deviation(data, average)
day_most_rain = find_day_most_rain(data)
year_most_rain = find_year_most_rain(data)

print(f'{len(data)} records')
print(f'Average rainfall: {average}cm')
print(f'Standard deviation: {standard_deviation}cm')
print(f'68% of the data will fall within {average-standard_deviation} - {average+standard_deviation}')
print(f'The day with the most rain was on {day_most_rain["day"]}/{day_most_rain["month"]}/{day_most_rain["year"]} with {day_most_rain["rain"]}cm')
print(f'The year with the most rain on average was {year_most_rain[0]} with {year_most_rain[1]}cm/day')

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






    


