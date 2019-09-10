# practice_1_fund_prob3.py

def near_100(num):
    if num > 90 <= 100:
        near_100 = True
    elif num >= 100 < 109:
        near_100 = True
    else:
        near_100 = False
    return near_100
    
user_num = float(input("Please enter a number: "))

if near_100(user_num) is True:
    print("\nYay! Your number is within 10 digits of 100.\n")
else:
    print("\nDarn, your number is NOT within 10 digits of 100.\n")