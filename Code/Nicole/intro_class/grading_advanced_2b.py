# Greeting
print("Find out what your grade is below.\n")
​
user_grade = input("What is your grade percentage? Please enter a number between 0 and 100: \n" )
​
user_grade = int(user_grade)
​
addon_grade = user_grade % 10
​
if addon_grade > 6:
    plus_minus = "+"
elif addon_grade < 4:
    plus_minus = "-"
else:
    plus_minus = ""
​
if user_grade in range(0,60):
    print("You got an F, maybe you should study harder.")
​
elif user_grade in range(60,70):
    print("You got a D, you didn't fail, but you should work harder.")
​
elif user_grade in range(70,80):
    print(f"You got a C{plus_minus}, you're doing okay but not great.")
​
elif user_grade in range(80,90):
    print(f"You got a B{plus_minus}. Good job!")
​
elif user_grade in range(90,101):
    print(f"Woo-hoo! You got an A{plus_minus}!")
​
else:
    print("Please enter a valid grade")
​
#Advanced version 2
