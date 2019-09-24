# lab_08_make_change.py

# URL :: https://github.com/PdxCodeGuild/class_honeybadger/blob/master/1%20Python/labs/lab08-make_change.md

def make_change_v1():
    user_input = input("How many pennies do you have?\n")
    user_input = int(user_input)
    quarters = (user_input // 100) * 4
    dimes = ((user_input % 100) - ((user_input % 100) % 10)) // 10
    nickels = ((user_input - (quarters * 25) - (dimes * 10)) - ((user_input - (quarters * 25) - (dimes * 10)) % 5)) // 5
    pennies = user_input - (quarters * 25) - (dimes * 10) - (nickels * 5)
    print(f"Quarters = {quarters}")
    print(f"Dimes = {dimes}")
    print(f"Nickels = {nickels}")
    print(f"Pennies = {pennies}")

def make_change_v2():
    user_dollars = input("Enter a dollar amount (ex. '1.36'):\n")
    user_dollars = float(user_dollars)
    user_input = user_dollars * 100
    user_input = int(user_input)
    quarters = (user_input // 100) * 4
    dimes = ((user_input % 100) - ((user_input % 100) % 10)) // 10
    nickels = ((user_input - (quarters * 25) - (dimes * 10)) - ((user_input - (quarters * 25) - (dimes * 10)) % 5)) // 5
    pennies = user_input - (quarters * 25) - (dimes * 10) - (nickels * 5)
    print(f"Quarters = {quarters}")
    print(f"Dimes = {dimes}")
    print(f"Nickels = {nickels}")
    print(f"Pennies = {pennies}")

make_change_v2()