# practice_1_fund_prob1.py

# define the function

def eve_or_odd(num):
    calc_num = num%2
    return calc_num

calc_num = input("Please enter a number: ")

if calc_num == 0:
    print("\nThat's an even number\n")
else:
    print("\nThat's an odd number\n")
        