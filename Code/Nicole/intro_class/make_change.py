# make_change.py

# dictionary

curr_dict = {
100: 1,
25: .25,
10: .10,
5: .05,
1: .01,
}

# ask user how many pennies they have
how_many = input("How many pennies do you have? ")

# change to integer
user_pennies = int(how_many)

# define variables
leftover_pennies = 0
amount = 0
dollars = 0
quarters = 0
dimes = 0
nickels = 0
pennies = 0

for key, value in curr_dict.items():
    if user_pennies >= key:
        # determines remaining pennies
        leftover_pennies = user_pennies % key
        # calculates the number of
        amount = (user_pennies - leftover_pennies)/key
        user_pennies -= (user_pennies - leftover_pennies)
        print(amount)
        print(f"Your change is {amount}")
