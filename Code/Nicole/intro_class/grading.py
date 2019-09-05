# Greeting

print("Find out what your grade is below.\n")

user_grade = input("What is your grade percentage? Please enter a number between 0 and 100: \n" )

user_grade = int(user_grade)

if user_grade in range(0,60):
    print("You got an F, maybe you should study harder.")

elif user_grade in range(60,70):
    print("You got a D, you didn't fail, but you should work harder.")

elif user_grade in range(70,80):
    print("You got a C, you're doing okay but not great.")

elif user_grade in range(80,90):
    print("You got a B. Good job!")

elif user_grade in range(90,101):
    print("Woo-hoo! You got an A!")

else:
    print("Please enter a valid grade")

print("\n")
