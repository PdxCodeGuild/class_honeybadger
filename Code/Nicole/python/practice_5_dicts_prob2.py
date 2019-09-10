# practice_5_dicts_prob2.py

# Using the result from the previous problem, iterate through the dictionary and calculate the average price of an item.

def combine(list_1, list_2):
    return dict(zip(list_1, list_2))

fruits = ['apple', 'banana', 'pear']
prices = [1.2, 3.3, 2.1]

print(combine(fruits, prices))

fruit_prices = combine(fruits, prices)

# solution

print(list(fruit_prices.values()))

def average(dict):
    return sum(list(dict.values())) / len(list(dict.values()))
    
print(average(fruit_prices))