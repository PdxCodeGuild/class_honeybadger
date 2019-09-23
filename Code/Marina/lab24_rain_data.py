
import requests
import re
import datetime as d
import math
import matplotlib.pyplot as plt


# this function will make data available and set date to dates of rain and rain to amounts of rain, converting rain from tips to inches. function also creates ourlist, appending it with readable dates using the datetime object. returns a dict.
def load_data(url):
    response = requests.get(url)
    response = response.text
    # regex to get the date and rainfall in a readable format
    new_response = re.findall('(\d{2}-\w{3}-\d{4})\s+(\d+)', response)
    ourlist = []
    # print(new_response)

    for i in range(len(new_response)):
        date = new_response[i][0]
        rain = new_response[i][1]
        # convert tips to inches to centimeters
        rain = int(rain)*.01*2.54
        # create new variable with date formatted
        date2 = d.datetime.strptime(date, '%d-%b-%Y')
        # create dict from date2 + rain
        ourlist.append({'year': date2.year, 'month': date2.month, 'day': date2.day, 'rain': rain})
    # print(ourlist)
    return ourlist


# measure average rainfall with the dict data
def find_average(data):
    total_days = 0
    total_rain = 0
    # itirate through dicts to create variable rain
    for i in range(len(data)):
        rain = data[i]['rain']
        # add all the rain toghether for accumulated rain.
        total_rain += rain
        # count rows(rain days)
        total_days +=1
    return total_rain/total_days


# standard deviation from data and average
def find_standard_deviation(data, average):
    total_days = 0
    total_variance = 0
    for i in range(len(data)):
        # again setting rain to rainfall
        rain = data[i]['rain']
        # calc the variance
        v = (rain - average)**2
        total_variance += v
        total_days += 1
    # print(total_variance)
    # print(total_days)
    # calc average (standart) deviation
    # return math.sqrt(total_variance/total_days)
    # an alternative square root method below
    return (total_variance/total_days)**0.5

# rainiest day
def most_rain(data):
    r = data[0]
    for row in data:
        if row['rain'] > r['rain']:
            r = row
    return r

# most_rain_record = most_rain(data)
# print(f'The day with the most rain was {most_rain_record["day"]}/{most_rain_record["month"]}/{most_rain_record["year"]}')
#
# print('The day with the most rain was ' + str(most_rain_record['day']) + '/' + str(most_rain_record['month']) + '/' + str(most_rain_record['year']) + ' ' + 'when' + ' ' + str(most_rain_record['rain']) + ' inches' + ' fell')

#Find day with most rain and rainfall by year.
def find_year_most_rain(data):
    years = []
    for row in data:
        # iterates through rows, if value of years is not in the list years, appends the value of key years to list for a list of unique find_year_most_rain
        if row['year'] not in years:
            years.append(row['year'])
            # then sort
            years.sort()
    totals = [0]*len(years)
    counts = [0]*len(years)

    for row in data:

        year_index = years.index(row['year'])
        totals[year_index] += row['rain']
        counts[year_index] += 1
    year_averages = []
    for year in years:
        data_year = [row for row in data if row['year'] == year]
        average = find_average(data_year)
        year_averages.append((year, average))
        return max(year_averages, key=lambda x:x[1])



# Function to plot
def plot_all_data(data):
    x_values = [d.datetime(row['year'],row['month'], row['day']) for row in data]
    y_values = [row['rain'] for row in data]
    plt.plot(x_values,y_values)

# function to show the plot
    plt.show()

data = load_data('https://or.water.usgs.gov/non-usgs/bes/shipyard.rain')
average = find_average(data)
standard_deviation = find_standard_deviation(data, average)
day_most_rain = most_rain(data)
year_most_rain = find_year_most_rain(data)
plot_all_data(data)
    # print(f'{len(data)} records')
print(f'Average: {average}')
print(f'Standard deviation: {standard_deviation}')
print(f'68% of the rain will fall within {average-standard_deviation} - {average + standard_deviation}')

# max_rain(data)
