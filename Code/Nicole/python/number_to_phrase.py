# number_to_phrase.py

def num_to_phrase(num):        
    ones = {
        1: "one", 
        2: "two", 
        3: "three", 
        4: "four", 
        5: "five", 
        6: "six", 
        7: "seven", 
        8: "eight", 
        9: "nine", 
        10: "ten"
        }
    teens = {
        1: "eleven", 
        2: "twelve", 
        3: "thirteen", 
        4: "fourteen", 
        5: "fifteen", 
        6: "sixteen", 
        7: "seventeen", 
        8: "eighteen", 
        9: "nineteen"
        }
    tens = {
        2: "twenty", 
        3: "thirty", 
        4: "forty", 
        5: "fifty", 
        6: "sixty", 
        7: "seventy", 
        8: "eighty", 
        9: "ninety"
        }
    
    phrase = ""
    
    if num <= 10:
        phrase += ones[num]
    elif num >10 and num <20:
        teen_num = num%10
        phrase += teens[teen_num]
    elif num >= 20 and num < 100:
        last_num = num % 10
        first_num = (num - last_num)//10
        phrase += tens[first_num]
        if last_num > 0:
            phrase += "-" + ones[last_num]
    elif num >= 100 and num <= 999:
        last_two_nums = num % 100
        print(f"Last two numbers: {last_two_nums}")
        first_hun_num = num//100 # returns first digit
        print(f"First digit: {first_hun_num}")
        last_hun_num = num % 10 # determines last number 
        print(f"Last number: {last_hun_num}")
        mid_hun_num = ((num - last_hun_num)//10) % 10 # determines middle number
        print(f"Middle number: {mid_hun_num}")
        if last_two_nums == 00:
            phrase += ones[first_hun_num] + " hundred"
        elif mid_hun_num == 0: # prints a hundres single-digit number (103, etc)
            phrase += ones[first_hun_num] + " hundred and " + ones[last_hun_num]
        elif mid_hun_num == 1: # prints a "teen" number (113, etc)
            phrase += ones[first_hun_num] + " hundred and " + teens[last_hun_num]
        else:
            phrase += ones[first_hun_num] + " hundred and " + tens[mid_hun_num] + "-" + ones[last_hun_num]
    return phrase

user_num = int(input("Please enter a number: "))
print(num_to_phrase(user_num))