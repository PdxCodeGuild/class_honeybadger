

# def make_change(a):

change = 0

user_input = float(input('Enter a dollar amount, please: '))
# print(user_input)
total = int(user_input * 100)
print(total)
# if total % 25 == 0:
quarters = total//25
total -= quarters*25

dimes = total//10
total -= dimes*10

nickels = total//5
total -= nickels*5


print(f"You have {quarters} quarters")

print(f"You have {quarters} quarters and {dimes} dimes and {nickels} nickels")



    # make_change(total=100)
