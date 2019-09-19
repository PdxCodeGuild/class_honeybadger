# test.py

from bokeh.plotting import figure, output_file, show

import requests
import re
import datetime
from statistics import variance

# prepare some data

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
    
    output_file("rain_data.html")

    p = figure(
       title = "Rainfall",
       x_axis_label = "Average Rainfall",
       y_axis_label = "Year"
    )
    p.line(x_values, y_values, line_width=2)
    
    return show(p)


loc = requests.get("https://or.water.usgs.gov/non-usgs/bes/mt_tabor.rain")
loc = loc.text
data = rain_data(loc)

print(f"The average rain in this location: {rain_mean(data)}")
print(f"The variance of rain is: {rain_variance(data)}")
print(f"The day with the most rain: {most_rain_day(data)}")
print(f"The year with the most rain: {most_rain_year(data)}")
print(rain_plot(data))