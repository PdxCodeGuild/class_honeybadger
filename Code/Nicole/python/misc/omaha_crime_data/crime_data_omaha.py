# crime_data_omaha.py

import csv
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, ranges, LabelSet
import re
import math

# csv index values:
# 0 - RB Number
# 1 - Reported Date
# 2 - Reported Time
# 3 - Statute/Ordinance Description (type)
# 4 - Occurred Location
# 5 - Occurred District
# 6 - Occurred Block LAT
# 7 - Occurred Block LON

def omaha_crime(data):
    with open(data, "r", newline = "") as csv_file:
        contents = list(csv.reader(csv_file))
    contents.pop(0) # removes the first row of labels
    return contents

def crime_chart(contents):
    temp_list = []
    crime_dict = {}
    crime_x = []
    crime_y = []
    
    index = input("What do you want to view?\n\tType '1' to view crime by date\n\tType '2' to view crime by type\n\tType '3' to view crime by district\n\tType '4' to view crime by time of day\n-->  ")
    if index == "1":
        index = 1
        x_string = "Date"
        y_string = "Number of incidents"
    elif index == "2":
        index = 3
        x_string = "Type of crime"
        y_string = "Number of incidents"
    elif index == "3":
        index = 5
        x_string = "District"
        y_string = "Number of incidents"
    elif index == "4":
        index = 2
        x_string = "Tme of day"
        y_string = "Number of incidents"
    
    # print(contents[1][index][:2])
    # exit()
    
    # creates a temporary list to sort so the x values are in order
    for i in range(len(contents)):
        if contents[i][index] not in temp_list:
            temp_list.append(contents[i][index])
            temp_list.sort()
    
    # adds the item to the dictionary with a count of "1"
    for i in range(len(temp_list)):
        if temp_list[i] not in crime_dict:
            crime_dict[temp_list[i]] = 1
    
    # counts the number of key items and updates the dictionary
    for key in crime_dict:
        for j in range(len(contents)):
            if contents[j][index] == key:
                crime_dict[key] += 1
    
    # creates lists out of the key/value pairs
    for key in crime_dict:
        crime_x.append(key)
        crime_y.append(crime_dict[key])
    
    # creates the chart
    output_file("omaha_crime.html")
    
    source = ColumnDataSource(dict(x = crime_x, y = crime_y))
    
    x_label = x_string
    y_label = y_string
    title = "Crime in Omaha, Nebraska"
    plot = figure(
        plot_width=4000, 
        plot_height=600, 
        tools="save, pan, zoom_in, zoom_out, reset",
        x_axis_label = x_label,
        y_axis_label = y_label,
        title = title,
        x_minor_ticks = 0,
        x_range = source.data["x"],
        y_range= ranges.Range1d(start = 0, end = max(crime_y)+(max(crime_y)/10))
        )
    
    plot.xaxis.major_label_orientation = math.pi/2

    
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
    
    

year = input("What year do you want to view? Choose between 2015 and 2019.\n-->  ")
data = omaha_crime(f"Incidents_{year}.csv")
crime_chart(data)
