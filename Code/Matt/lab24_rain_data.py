import requests
import re



def rain_data(url):

    response = requests.get(url)
    rain_file = response.text
    pattern = r"(\d{2}-\w{3}-\d{4})\s+(\d+)"
    find_rain = re.findall(pattern, rain_file)
    return find_rain


def convert(tup):
    dictionary = {}
    for a, b in tup:
        dictionary.setdefault(a, []).append(b)

    return dictionary




url = 'https://or.water.usgs.gov/non-usgs/bes/albina.rain'
# print(rain_data(url))
# print(convert(rain_data(url)))
