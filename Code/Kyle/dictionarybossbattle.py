
import string

d = {'a1':5, 'a2':2, 'a3':3, 'b1':10, 'b2':1, 'b3':1, 'c1':4, 'c2':5, 'c3':6}

def calc_average():
    d = list(a_dict.values())
    return round(sum(prices) / len(prices))

def average_key(a_dict):
    results = {}
    for letter in string.ascii_lowercase:
        count = 0
        total = 0
        for key in a_dict:
            if not key.startswith(letter):
                continue
            count += 1
            total += a_dict[key]
            results.update({letter: (total / count)})

            calc_average(a_dict)
            d = list(a_dict.values())
            return round(sum(prices) / len(prices))
        return results

print(average_key(d))
