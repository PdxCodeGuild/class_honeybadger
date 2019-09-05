# make_change2.py

import math
import sys

# ask user how many pennies they have
user_pennies = input("\nHow many pennies do you have? ")

if user_pennies.isdigit():
    print()
else:
    print("\nPlease enter a number.\n")
    sys.exit()

# change to integer
user_pennies = int(user_pennies)

# define variables
dollars = 0
quarters = 0
dimes = 0
nickels = 0
pennies = 0

# converts to a floast
user_pennies = user_pennies / 100

#test print
print(f"You have ${user_pennies}\n")

while user_pennies > 1:
    if user_pennies >= 1.00:
        calc_dollars = math.trunc(user_pennies)
        dollars += calc_dollars
        user_pennies = user_pennies - math.trunc(user_pennies)
    else:
        pass
    if user_pennies >= .25:
        calc_quarters = math.trunc(user_pennies / .25)
        quarters += calc_quarters
        user_pennies = user_pennies - (.25 * quarters)
    else:
        pass
    if user_pennies >= .10:
        calc_dimes = math.trunc(user_pennies / .10)
        dimes += calc_dimes
        user_pennies = user_pennies - (.10 * dimes)
    else:
        pass
    if user_pennies >= .05:
        calc_nickels = math.trunc(user_pennies / .05)
        nickels += calc_nickels
        user_pennies = user_pennies - (.05 * nickels)
    else:
        pass
    if user_pennies >= .01:
        calc_pennies = math.trunc(user_pennies / .01)
        pennies += calc_pennies
    else:
        pass
else:
    print("Here's your change:\n")

print(f"You get {dollars} dollars, {quarters} quarters, {dimes} dimes, {nickels} nickels, and {pennies} pennies.\n")
