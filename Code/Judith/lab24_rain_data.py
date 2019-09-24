# filename: lab24_rain_data.py

import requests
import re
import datetime
import matplotlib.pyplot as plt

response = requests.get('https://or.water.usgs.gov/non-usgs/bes/mt_tabor.rain')
page = response.text
#print(page)
date_total = re.findall(r'(\d{2}-\w{3}-\d{4})\s+(\d+)',page)

# legible print of date_total
# print('\n'.join([str(date_total[i]) for i in range(len(date_total))]))

# testing datetime object
# datetest = datetime.datetime.strptime(dates[0], '%d-%b-%Y')
# print(datetest)

dates = [datetime.datetime.strptime(str(date_total[i][0]), '%d-%b-%Y') for i in range(len(date_total))]
totals = [int(date_total[i][1]) for i in range(len(date_total))]



def find_record_year(dates, totals):
    years = list(set(dates[i].year for i in range(len(dates))))
    year_totals = [0 for i in range(len(years))]
    year_counts = [0 for i in range(len(years))]
    year_avgs = [0 for i in range(len(years))]
    
    for i in range(len(years)):
        for j in range(len(dates)):
            if dates[j].year == years[i]:
                year_counts[i] += 1
                year_totals[i] += totals[j]
        year_avgs[i] = year_totals[i] / year_counts[i]
    # print(years,'\n',year_counts,'\n',year_totals,'\n',year_avgs)
    # print(len(years) == len(year_totals) == len(year_counts) == len(year_avgs))

    return years[year_avgs.index(max(year_avgs))]

def find_variance(dates, totals):
    avg_rainfall = sum(totals)/len(totals)
    total_variance = 0
    total_days = 0
    for i in range(len(totals)):
        v = (totals[i]-avg_rainfall)**2
        total_variance += v
        total_days +=1
    return (total_variance/total_days)**0.5

print(f'data variance: {find_variance(dates, totals)}')
record_year = find_record_year(dates, totals)
record_day = dates[totals.index(max(totals))]
print(f'record year: {record_year}')
print(f'record day: {record_day, max(totals)}')

plt.plot(dates, totals)
plt.show()




    


