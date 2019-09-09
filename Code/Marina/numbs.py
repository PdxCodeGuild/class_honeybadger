def nums_to_phrase(num):
    if num <= 10:
        print(singles[num])
    elif num <= 19:
        print(teens[num])
    elif num < 100:
        tens_digit = num//10
        ones_digit = num%10
        print(tens[tens_digit] + singles[ones_digit])
    elif num > 100:
        hundred_digit = num//100
        ones_digit = num%10
        tens_digit = ((num - ones_digit)//10) % 10
        round_hundreds = hundred_digit % 100
        print(singles[hundred_digit] + ' ' + 'hundred' + ' ' + tens[tens_digit] + ' ' + singles[ones_digit])
    elif num 
        # hundred_digit = num//100
        # ones_digit = num%10
        # tens_digit = ((num - ones_digit)//10) % 10
        # round_hundreds = hundred_digit % 100
        # print (hundred_digit)
        # print(singles[hundred_digit] + ' ' + 'hundred')


singles = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'}

tens = {2: 'twenty', 3: 'thirty', 4: 'fourty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}

teens = {11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}

list(singles.values())
list(tens.values())

user_input = int(input('give me a number between 1 and 999: '))
nums_to_phrase(user_input)
