# lab_24_rain_data.py

import requests
import re
import datetime
from statistics import variance
import matplotlib.pyplot as plt

def rain_data(location):
    pattern = "(\d{2}-\w{3}-\d{4})\s+(\d+)"
    find_rain = re.findall(pattern, location)
    rain_list = []
    for x, y in find_rain:
        x = x.split("-")
        month_list = ["", "JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
        for i in range(len(month_list)):
            if x[1] == month_list[i]:
                x_month = i
        x_day = int(x[0])
        x_year = int(x[2])
        rain_date = datetime.datetime(x_year, x_month, x_day)
        # rain_date.strftime('%b %d %Y')
        rain_list.append([rain_date, int(y)])
    return rain_list


def rain_mean(mean_list):
    calc_mean = []
    for a in range(len(mean_list)):
        calc_mean.append(int(mean_list[a][1]))
    return float(sum(calc_mean)) / max(len(calc_mean), 1)

    
def rain_variance(mean_list):
    calc_mean = []
    for b in range(len(mean_list)):
        calc_mean.append(int(mean_list[b][1]))
    return variance(calc_mean) 


def most_rain_day(most_rain_list):
    rain = 0
    rain_day = ""
    for c in range(len(most_rain_list)):
        if int(most_rain_list[c][1]) > rain:
            rain = int(most_rain_list[c][1])
    for d in range(len(most_rain_list)):
        if int(most_rain_list[d][1]) == rain:
            rain_day = most_rain_list[d][0]
    return rain_day


def most_rain_year(most_rain_year):
    rain_year_list = []
    rain_year = []
    rain_count = 0
    
    for e in range(len(most_rain_year)):
        # rain_year += (most_rain_year[e][1])
        if most_rain_year[e][0].year not in rain_year_list:
            rain_year_list.append(most_rain_year[e][0].year)
    
    for f in range(len(rain_year_list)):
        for g in range(len(most_rain_year)):
            if rain_year_list[f] == most_rain_year[g][0].year:
                rain_count += most_rain_year[g][1]
            # print(rain_count)
        rain_year.append(rain_count)
        rain_count = 0
    
    for h in range(len(rain_year_list)):
        for i in range(len(rain_year)):
            if rain_year[i] == max(rain_year):
                max_year = rain_year_list[i]
    
    return max_year


def rain_plot(rain_plot_chart):
    x_values = []
    y_values = []
    
    
    for e in range(len(rain_plot_chart)):
        # rain_year += (most_rain_year[e][1])
        if rain_plot_chart[e][0].year not in x_values:
            x_values.append(rain_plot_chart[e][0].year)
    
    for f in range(len(x_values)):
        rain_count = 0
        for g in range(len(rain_plot_chart)):
            if x_values[f] == rain_plot_chart[g][0].year:
                rain_count += rain_plot_chart[g][1]
            # print(rain_count)
        y_values.append(rain_count)
    
    plt.plot(x_values, y_values)
    return plt.show()

def rain_plot_days(rain_plot_chart_days):
    x_values = []
    y_values = []
    rain_count = 0
    
    for a in range(len(rain_plot_chart_days)):
        # print(rain_plot_chart_days[a][0].month)
        # print(rain_plot_chart_days[a][1])
        # exit()
        if rain_plot_chart_days[a][0].year == 2018:
            x_values.append(rain_plot_chart_days[a][0])
            y_values.append(rain_plot_chart_days[a][1])
    print(x_values)
    
    # 
    plt.plot(x_values, y_values)
    return plt.show()

def rain_plot_day_avg(rain_plot_day_avg):
    x_values = []
    y_values = []
    d_values = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    for a in range(len(rain_plot_day_avg)):
        if rain_plot_day_avg[a][0].weekday() not in x_values:
            x_values.append(rain_plot_day_avg[a][0].weekday())
        
    for b in range(len(x_values)):
        rain_count = 0
        count = 0
        for c in range(len(rain_plot_day_avg)):
            if x_values[b] == rain_plot_day_avg[c][0].weekday():
                count += 1
                rain_count += rain_plot_day_avg[c][1]
        rain_count = rain_count / count
        y_values.append(rain_count)
    
    # y_values.replace(0, "Monday")
    
    
    plt.bar(d_values, y_values, color = "g")
    plt.ylabel("Average rainfall (in \"tips\")", color = "b")
    plt.xlabel("Days of the week", color = "r")
    return plt.show()
    


loc = requests.get("https://or.water.usgs.gov/non-usgs/bes/mt_tabor.rain")
loc = loc.text

# print(*rain_data(loc))


data = rain_data(loc)

# data_1998 = [row for row in data if row[0].year == 1998]
# print(data_1998)

# print(f"The average rain in this location: {rain_mean(data)}")
# print(f"The variance of rain is: {rain_variance(data)}")
# print(f"The day with the most rain: {most_rain_day(data)}")
# print(f"The year with the most rain: {most_rain_year(data)}")
print(rain_plot_day_avg(data))



#

