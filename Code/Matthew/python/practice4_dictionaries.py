


def combine(keys, values):
    # return dict(zip(keys, values))
    
    matthews_fruits = {}
    for i in range(len(keys)):
        matthews_fruits[keys[i]] = values[i]
    return matthews_fruits


def average(dictionary):
    
    total = 0
    for key in dictionary:
        total += dictionary[key]
    return total / len(dictionary)
    
    # return sum(dictionary.values())/len(dictionary)


def find_key_for_value(dictionary, value):
    for key in dictionary:
        if dictionary[key] == value:
            return key
    return None

# d = {'apple': 1.2, 'banana': 3.3}
# # d['pear'] # crash
# 
# if 'pear' in d:
#     pear_value = d['pear']
# else:
#     pear_value = 0
# 
# pear_value = d.get('pear', 0)
# print(pear_value)




#           0         1         2
fruits = ['apple', 'banana', 'pear']
prices = [1.2,      3.3,      2.1]
combined = combine(fruits, prices)
# print(combine(fruits, prices)) # {'apple':1.2, 'banana':3.3, 'pear':2.1}

# print(average(combined)) # 2.2



def unify(dictionary):
    totals = {}
    counts = {}
    for key in dictionary:
        # key == 'a1'
        # dictionary[key] == 5
        
        letter = key[0] # a
        
        if letter in totals:
            totals[letter] += dictionary[key]
            counts[letter] += 1
        else:
            totals[letter] = dictionary[key]
            counts[letter] = 1
        
        # print(letter, key, dictionary[key])
        # print(totals)
        # print(counts)
        # print()
    
    averages = {}
    for key in totals:
        average = totals[key] / counts[key]
        averages[key] = average
    return averages



d = {'a1':5, 'a2':2, 'a3':8,
     'b1':10, 'b2':1, 'b3':1,
     'c1':4, 'c2':5, 'c3':6,
     'z4':3}
print(unify(d)) # {'a':3.33333333, 'b':4, 'c':5}









