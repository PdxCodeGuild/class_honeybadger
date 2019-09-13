#Make Change


user_pennies = int(input("How many pennies do you have? "))

num_quarters = user_pennies // 25
pennies = user_pennies % 25

print(f"You have {num_quarters} quarters")
print(f"and {pennies} pennies")
