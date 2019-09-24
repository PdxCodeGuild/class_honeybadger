

user_input = float(input('Enter a dollar amount, please: '))
total = int(user_input * 100)
# print(total)
quarters = total//25
total -= quarters*25

dimes = total//10
total -= dimes*10

nickels = total//5
total -= nickels*5

pennies = total

print(f"{quarters} in quarters")
print(f"{dimes} in dimes")
print(f"{nickels} in nickels")
print(f"{pennies} in pennies")

print(f"You have {quarters} in quarters and {dimes} in dimes and {nickels} in nickels and {pennies} in pennies")
