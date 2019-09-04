


# def add(a, b):
#     return a + b
# 
# add = lambda a, b: a + b
# 
# print(add(5, 2))
# 
# data = [('apple', 1.0), ('banana', 0.5), ('cherries', 0.1)]
# print(data)
# data.sort(key=lambda x: x[1])
# print(data)











# receive an integer as a parameter
# return the string representing the number or None
def number_to_phrase(num):

    ones_teens = ['zero', 'one', 'two', 'three', 'four', 'five',
                    'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
                    'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
                    'seventeen', 'eighteen', 'nineteen']
    #       0   1      2        3          4        5
    tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    if num <= 19:
        return ones_teens[num]
    elif num <= 99:
        ones_digit = num % 10
        tens_digit = num // 10
        
        # num = str(num)
        # ones_digit = int(num[0])
        # tens_digit = int(num[1])
        
        if ones_digit == 0:
            return tens[tens_digit]
        return tens[tens_digit] + '-' + ones_teens[ones_digit]
    elif num <= 999:
        ones_digit = num % 10
        tens_digit = (num // 10) % 10
        hundreds_digit = num // 100
        
        if tens_digit == 0:
            if ones_digit == 0:
                return ones_teens[hundreds_digit] + '-hundred'
            return ones_teens[hundreds_digit] + '-hundred and ' + ones_teens[ones_digit]
        elif tens_digit == 1:
            return ones_teens[hundreds_digit] + '-hundred and ' + ones_teens[10+ones_digit]
        
        if ones_digit == 0:
            return ones_teens[hundreds_digit] + '-hundred and ' + tens[tens_digit]
        
        return ones_teens[hundreds_digit] + '-hundred and ' + tens[tens_digit] + '-' + ones_teens[ones_digit]
        
        
        
        
        
    
    return None




# if x == 0:
#     print('zero')
# elif x == 1:
#     print('one')
# # ...
# elif x == 999:
#     print('nine hundred and ninety-nine')

import random

if __name__ == '__main__':
    
    
    # for i in range(10):
    #     r = random.randint(0, 99)
    #     print(r, number_to_phrase(r))
    
    for i in range(0, 1000):
        print(i, number_to_phrase(i))
    
    # x = int(input('enter a number: '))
    # print(number_to_phrase(x))
    
    # assert number_to_phrase(19) == 'nineteen'
    # for i in range(30):
    #     print(number_to_phrase(i))
    


