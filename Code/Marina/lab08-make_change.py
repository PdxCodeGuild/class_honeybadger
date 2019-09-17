

user_input = float(input('Enter a dollar amount, please: '))
total = int(user_input * 100)
print(total)
quarters = total//25
total -= quarters*25

dimes = total//10
total -= dimes*10

nickels = total//5
total -= nickels*5

pennies = total

print(f"{quarters} quarters")
print(f"{dimes} dimes")
print(f"{nickels} nickels")
print(f"{pennies} pennies")

print(f"You have {quarters} quarters and {dimes} dimes and {nickels} nickels and {pennies} pennies")
