# test.py

# This code pulls data from the Oregon website that displays data charts of daily rainfall.

from bokeh.plotting import figure, output_file, show
import requests
import re
import datetime
from statistics import variance

# Pulls the rain data (date, rainfall) and separates it into a python-readable format. Also converts "tips" to "inches".

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
        y = float(y)
        y = y*0.01
        rain_list.append([rain_date, float(y)])
    return rain_list


# Returns the average daily rainfall 

def rain_mean(mean_list):
    calc_mean = []
    for a in range(len(mean_list)):
        # calc_mean.append(int(mean_list[a][1]))
        calc_mean.append(mean_list[a][1])
    return float(sum(calc_mean)) / max(len(calc_mean), 1)

    
# Returns the varaince (whatever that means, thank goodness for statistc methods)

def rain_variance(mean_list):
    calc_mean = []
    for b in range(len(mean_list)):
        calc_mean.append(mean_list[b][1])
    return variance(calc_mean) 


# Returns the day that received the most rain.

def most_rain_day(most_rain_list):
    rain = 0.0
    rain_day = ""
    for c in range(len(most_rain_list)):
        if most_rain_list[c][1] > rain:
            rain = most_rain_list[c][1]
    for d in range(len(most_rain_list)):
        if most_rain_list[d][1] == rain:
            rain_day = most_rain_list[d][0]
    return rain_day


# Returns the year that got the most rain overall.

def most_rain_year(most_rain_year):
    rain_year_list = []
    rain_year = []
    rain_count = 0.0
    
    for e in range(len(most_rain_year)):
        # rain_year += (most_rain_year[e][1])
        if most_rain_year[e][0].year not in rain_year_list:
            rain_year_list.append(most_rain_year[e][0].year)
    
    for f in range(len(rain_year_list)):
        for g in range(len(most_rain_year)):
            if rain_year_list[f] == most_rain_year[g][0].year:
                rain_count += most_rain_year[g][1]
        rain_year.append(rain_count)
        rain_count = 0
    
    for h in range(len(rain_year_list)):
        for i in range(len(rain_year)):
            if rain_year[i] == max(rain_year):
                max_year = rain_year_list[i]
    
    return max_year


# Creates a

def rain_plot(rain_plot_chart):
    x_values = []
    y_values = []
    
    for e in range(len(rain_plot_chart)):
        if rain_plot_chart[e][0].year not in x_values:
            x_values.append(rain_plot_chart[e][0].year)
    
    for f in range(len(x_values)):
        rain_count = 0.0
        for g in range(len(rain_plot_chart)):
            if x_values[f] == rain_plot_chart[g][0].year:
                rain_count += rain_plot_chart[g][1]
            # print(rain_count)
        y_values.append(rain_count)
    
    output_file("rain_data.html")

    p = figure(
       title = "Rainfall",
       plot_width = 1200,
       plot_height = 600,
       y_axis_label = "Average Rainfall (in inches)",
       x_axis_label = "Year",
       tools = "save"
    )
    # p.line(x_values, y_values, line_width=2)
    p.vbar(
        x = x_values,
        top = y_values,
        width = .7,
        bottom = 0,
        color = "blue",
        fill_alpha = 0.5
    )
    
    return show(p)

def rain_plot_days(data, year):
    x_values = []
    y_values = []
    # rain_count = 0
    year = int(year)
    
    for a in range(len(data)):
        if data[a][0].year == year:
            x_values.append(int(data[a][0].strftime('%m')))
            # x_values.append(data[a][0])
            y_values.append(data[a][1])

            
    
    p = figure(
       title = f"Average rainfall throughout {year}",
       plot_width = 1200,
       plot_height = 600,
       y_axis_label = "Average Rainfall (in inches)",
       x_axis_label = f"Months in {year}",
       tools = "save, zoom_in, zoom_out, pan, box_select"
    )
    # p.line(x_values, y_values, line_width=2)
    p.vbar(
        x = x_values,
        top = y_values,
        width = .7,
        bottom = 0,
        color = "firebrick",
        fill_alpha = 1
    )
    
    return show(p)


# the URL here is the data for this code. Change the URL to a different data table to see other locations: https://or.water.usgs.gov/non-usgs/bes/

loc = requests.get("https://or.water.usgs.gov/non-usgs/bes/mt_tabor.rain")
loc = loc.text
data = rain_data(loc)

print(f"The average rain in this location: {rain_mean(data)}")
print(f"The variance of rain is: {rain_variance(data)}")
print(f"The day with the most rain: {most_rain_day(data)}")
print(f"The year with the most rain: {most_rain_year(data)}")
rain_plot(data)
rain_plot_days(data, 2012)