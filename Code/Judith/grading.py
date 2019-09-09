#filename: grading.py

'''Lab 4: Grading

Let's convert a number grade to a letter grade, using if and elif statements and comparisons.

    Have the user enter a number representing the grade (0-100) ..use input()
    Convert the number grade to a letter grade

Numeric Ranges

    90-100: A
    80-89: B
    70-79: C
    60-69: D
    0-59: F

Advanced Version 1

Use randint() from the random module to determine the user's rival's score. Let the user know if they did better than their rival.'''

#random module imported for rival test
import random

#filename: grading.py
#user prompt
grade1=input("Enter grade between 0 and 100: ")
print(f"You entered a score of ", grade1)


#function to determine if input is a valid
def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
#protection from improper input
if isFloat(grade1):
    grade1=float(grade1)
    yga=("Your letter grade is: ")

    #rival grade
    grade2=random.uniform(0,100)

    #sorting instructions
    if 89<grade1<=100:
        print(yga, "A")

    elif 79<grade1<89:
        print(yga, "B")

    elif 69<grade1<79:
        print(yga, "C")

    elif 59<grade1<69:
        print(yga, "D")

    elif grade1<=59:
        print(yga, "F")

    print("Your rival's score was", grade2)

    if grade1>grade2:
        print("You did better than your rival!")

    else:
        print("Your rival has beaten you :(")

else:
    print("Please enter a valid input")
