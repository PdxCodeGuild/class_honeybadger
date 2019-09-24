# lab_optional_crime_data.py

# URL :: https://github.com/PdxCodeGuild/class_honeybadger/blob/master/1%20Python/labs/optional-crime_data.md

import csv
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, ranges, LabelSet
import re
import math

def crime_data(data):
    with open(data, "r", newline = "") as csv_file:
        contents = list(csv.reader(csv_file))
    
    crime_list = []
    
    for i in range(1, len(contents)):
        crime_list.append(contents[i])
    
    return crime_list

# 0-location, case_number, crime_against, measure_names, neighborhood, occur_date, occur_time, offense_category, offense_type, offense_count

def crime_in_neighborhood(data):
    crime_dict = {}
    x_values = [] # neighborhood names
    y_values = [] # number of occurrances
    
    # creates a dictionary, gives each location one incident
    for i in range(len(data)):
        if data[i][4] not in y_values:
            crime_dict[data[i][4]] = 1
    
    # counts the number of incidents and updates the dictionary
    for key in crime_dict:
        for j in range(len(data)):
            if data[j][4] == key:
                crime_dict[key] += 1
    
    # creates lists of the two items for x and y values
    for key in crime_dict:
        x_values.append(key)
        y_values.append(crime_dict[key])
    
    # this creates the chart using Bokeh
    output_file("crime_data.html")
    
    source = ColumnDataSource(dict(x = x_values, y = y_values))
    
    x_label = "Neighborhoods"
    y_label = "Number of crime incidents"
    title = "Crime in Portland, Oregon"
    plot = figure(
        plot_width=4000, 
        plot_height=700, 
        tools="save, pan, zoom_in, zoom_out, reset",
        x_axis_label = x_label,
        y_axis_label = y_label,
        title = title,
        x_minor_ticks = 0,
        x_range = source.data["x"],
        y_range= ranges.Range1d(start = 0, end = 13000)
        )
    
    plot.xaxis.major_label_orientation = math.pi/3

    
    labels = LabelSet(
        x = "x",
        y = "y",
        text = "y",
        level = "glyph",
        x_offset = -15,
        y_offset = 5,
        source = source,
        render_mode="canvas",
        text_font_size="8pt"
        )

    plot.vbar(
        source = source,
        x = "x",
        top = "y",
        bottom = 0,
        width = 0.75,
        color = "firebrick",
        fill_alpha = 0.5
        )

    plot.add_layout(labels)
    show(plot)
    
    
    
    
    
    
    
    
    
    # p = figure(
    #    title = "Crime in Portland",
    #    plot_width = 1200,
    #    plot_height = 600,
    #    y_axis_label = "Number of crime incidents",
    #    x_axis_label = "Neighborhood",
    #    tools = "save"
    # )
    # p.line(x_values, y_values, line_width=2)
    # # p.vbar(
    # #     x = x_values,
    # #     top = y_values,
    # #     width = .7,
    # #     bottom = 0,
    # #     color = "blue",
    # #     fill_alpha = 0.5
    # # )
    # 
    # 
    # 
    # return show(p)
    

    
data = crime_data("crime_data.csv") # this pulls from the csv and runs the function to pull the data
crime_in_neighborhood(data) # this creates the chart for this function