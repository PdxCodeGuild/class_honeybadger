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






def day_most_rain(data):
    current_data = data[0]
    for i in range(len(data)):
        if data[i]['rain'] > current_data['rain']:
            current_data = data[i]
    return current_data






def year_most_rain(data):
    years = []
    for row in data:
        if row['year'] not in years:
            years.append(row['year'])
        years.sort()


    totals = []
    counts = []
    for i in range(len(years)):
        totals.append(0)
        counts.append(0)




    for row in data:
        year_index = years.index(row['year'])
        totals[year_index] += row['rain']
        counts[year_index] += 1


    # print(row)
    # print(years)
    # print(totals)
    # print(counts)

    year_averages = []
    for year in years:
        data_year = [row for row in data if row['year'] == year]
        average = find_average(data_year)
        year_averages.append((year, average))

    return max(year_averages, key=lambda x: x[1])

# def plot_points(data):
#     x_values = [datetime.datetime(row['year'])]
#     plt.plot(x_values, y_values)
#     plt.show









data = load_data('https://or.water.usgs.gov/non-usgs/bes/hayden_island.rain')
# print(data)
most_rain = day_most_rain(data)

average = find_average(data)
standard_deviation = find_standard_deviation(data, average)
day_record = day_most_rain(data)
record_year = year_most_rain(data)
print(f'{len(data)} records')
print(f'Average: {average}')
print(f'Standard deviation: {standard_deviation}')


# print(f'68% of the data will fall within {average-standard_deviation} - {average+standard_deviation}')


print(f'the day with most rain was: {day_record["day"]}/{day_record["month"]}/{day_record["year"]} The amount of rain that fell was {day_record["rain"]} inches')
print(f'the year with the most rain on average was: {record_year}')
