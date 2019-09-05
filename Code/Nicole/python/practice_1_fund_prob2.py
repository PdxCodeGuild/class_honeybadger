# practice_1_fund_prob2.py

# define the function

def pos_neg(a, b):
    if a < 0 and b > 0:
        pos_neg = True
    elif a > 0 and b < 0:
        pos_neg = True
    elif a < 0 and b < 0:
        pos_neg = False
    elif a > 0 and b > 0:
        pos_neg = False
    return pos_neg

user_num_1 = float(input("Please enter a number: "))
user_num_2 = float(input("Please enter another number: "))

if pos_neg(user_num_1, user_num_2) is True:
    print("Your numbers opposites.")
else:
    print("Your numbers are NOT opposites.")