
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
    for i in range(len(new_response)): #retruns a list of tuples 
        date = new_response[i][0] #takes tuple and returns position 0, which is the date
        rain = new_response[i][1] #takes tuple and returns position 1, which is rainfall
        rain = int(rain)*.01 #converts tips to inches
        #print(date, rain)
        
        date2 = d.datetime.strptime(date, '%d-%b-%Y') #conveting the date into specific format
        
        ourlist.append({'year': date2.year, 'month': date2.month, 'day': date2.day, 'rain': rain}) #appending and arranging the dictionary 
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

#Part A = Finds day with most rainfall in inches. 
def max_rain(data):
    dict_sort = sorted(data, key = lambda i: i['rain'])  #---> using lambda to find the day with the most rain.  lamda i:i is a required parameter. so it takes a parameter (first i) and second i focuses on a parameter
    #dict_sort = sorted(data, key = lambda i: i['rain'], reverse=True) #reverse not working 
    #print(dict_sort)

    #Part B = Finds the year which had the most rain.
    mylist = []
    for i in range(len(data)):
        mylist.append({'year': data[i]['year'], 'rain': data[i]['rain']}) #adding year and rain as a dictionary to mylist, 
                                                                          #result will be a list of dictionaries ['{year:1998, 'rain:0.0}, {year:1987, 'rain:1.0}]
    #print(mylist)

    # Collections are containers that are used to store collections of data (ie, list, dict, set, tuples)
    # Defaultdict works exactly like a dictionary, except it does not throw a keyerror when you try to access a non-existent key. 
    # Instead, it initializes the key with the element of the data type that you pass as an argument at the creation of defaultdict. 
    # The data type is called default_factory.
    # With defaultdict, need to specify a data type as an argument.

    #Process takes the list of dictionaries from mylist and summarizes the rainfall by year. 
    from collections import defaultdict 
    c = defaultdict(int)  #---> creating a defaultdict with a defaultdict constructor 
    for d in mylist: 
        c[d['year']] += d['rain']  #---> defining values for the keys year and rain.  Returns rain total by year.
    print(c) 
    # return c

    #To convert resutls to list of dictionaries:
    #print([{'Year': year, 'rain': rain} for year,rain in c.items()])

    yearlist = []
    totallist = []
    for year in c: #---> c references the defaultdict constructor. When iterating over a dictionary, the "index" will return the key, so this returns 2019, 2018, 2017, etch
        total = c[year] #---> this returns value of the key year, so returns the rainfall 
        yearlist.append(year)
        totallist.append(total)
    return yearlist, totallist
        
    print(yearlist)  #---> can be used as an axis for chart
    print(totallist) #---> can be used as an axis for chart
    # print(year)

#Creating Charts Optional ---Call max_rain function above to retrieve yearlist/total list for x,y axis. Or create chart within max_rain function
import matplotlib.pyplot as plt
def create_chart(x,y):
    # # x-axis values 
    # x = [5, 2, 9, 4, 7] 
  
    # # Y-axis values 
    # y = [10, 5, 8, 4, 2] 
  
    # Function to plot 
    plt.plot(x,y) 
  
    # function to show the plot 
    plt.show() 

    
#Calling functions   
data = load_data('https://or.water.usgs.gov/non-usgs/bes/hayden_island.rain')    
#print(data)
average = find_average(data)
standard_deviation = find_standard_deviation(data, average)
print(f'{len(data)} records')
print(f'Average: {average}')
print(f'Standard deviation: {standard_deviation}')
print(f'68% of the data will fall within {average-standard_deviation} - {average+standard_deviation}')

maxx_rain = max_rain(data)

#x and y axis/parameters for create_chart function
x = [5, 2, 9, 4, 7] 
y = [10, 5, 8, 4, 2]  
  
#create_chart(x,y) #---> passing x, y to function

      

    #Misc code for max_rain function.  Code was not summing by year. Appears to be returning a single value for year and single value for rain

    # Approach 1 = import collections
    
    # counter = collections.Counter() 
    # for d in mylist:  
    #     counter.update(d) 
      
    # result = dict(counter) 
    
    # print("dictionary : ", str(counter)) 
    # print(result)
    
    #Approach 2 = from operator import itemgetter
    # result = {}
    # for d in mylist: 
    #     for k in d.keys(): 
    #         result[k] = result.get(k, 0) + d[k] 
    
    # print("dictionary : ", str(result)) 

    # sum the values with same keys 


    # year = data[i]['year']
    # rain = data[i]['rain'] 
    # print(year)
    # print(rain)

# fruits = {'apples': 1.0, 'bananas': 0.5, 'pears': 0.75}
# for fruit in fruits:
#     print(fruit) # apples, bananas, pears
#     print(fruits[fruit]) # 1.0, 0.5, 0.75

        
        
    
 
        
    
    



