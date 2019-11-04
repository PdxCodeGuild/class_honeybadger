import requests
import re
import datetime
import matplotlib.pyplot as plt


url = 'https://or.water.usgs.gov/non-usgs/bes/albina.rain'

data_dict =[]

def load_data(url):

    response = requests.get(url)
    rain_file = response.text
    pattern = r"(\d{2}-\w{3}-\d{4})\s+(\d+)"
    rain_data = re.findall(pattern, rain_file)

    for date_str, rain_str in rain_data:
        date = datetime.datetime.strptime(date_str, '%d-%b-%Y')
        data_dict.append({'year': date.year, 'month': date.month, 'day': date.day, 'rain': int(rain_str)})

    return data_dict

def mean(data):
    total_rain = 0
    days = 0
    for i in range(len(data)):
        rain = data[i]['rain']
        total_rain += rain
        days += 1
    return total_rain/days


def plotter():
    rain_list = []
    dates_list = []
    for i in range(len(data)):
        rain_list.append(data[i]['rain'])
    for i in range(len(data)):
        date = datetime.datetime(data[i]['year'],data[i]['month'],data[i]['day'])
        dates_list.append(date)



    # print(rain_list)
    # plt.plot(dates_list,rain_list)
    plt.bar(dates_list,rain_list)
    plt.show()





data = load_data(url)
print(mean(data))
plotter()
