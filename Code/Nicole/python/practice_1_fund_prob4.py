# practice_1_fund_prob4.py

# define function

def max_of_three(a, b, c):
    if a > b and a > c:
        max_num = a
    elif b > a and b > c:
        max_num = b
    elif c > a and c > b:
        max_num = c
    return max_num
    
user_num_a = float(input("\nPlease enter a number: "))
user_num_b = float(input("\nPlease enter a second number: "))
user_num_c = float(input("\nPlease enter a third number: "))

user_max_num = max_of_three(user_num_a, user_num_b, user_num_c)

print(f"\nThe max number of the three is {user_max_num}.\n")