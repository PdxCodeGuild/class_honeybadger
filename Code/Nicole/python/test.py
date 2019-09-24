# test.py

import time

contents = ["00:01:23", "13:34:22", "22:12:34", "00:56:22", "13:22:39", "13:00:03"]

time_list = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "potato"]

time_dict = {"00" : 1, "potato" : 1, "13:34:22" : 1, "22:12:34" : 1, "00:56:22" : 1, "13:22:39" : 1, "13:00:03" : 1 }

new__dict = {}
new_list = []

for i in range(len(contents)):
    hour = time.tm_hour(contents[i])
    print(hour)
    hour_num = hour.strftime('%H')
    # hour = contents[i].strftime("%H")
    print(hour_num)
    new_list.append(hour_num)
    

print(new_list)