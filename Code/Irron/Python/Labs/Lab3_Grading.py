'''
Lab 3: Grading

Let's convert a number grade to a letter grade, using if and elif statements and comparisons.
Concepts Covered

    input, print
    type conversion (str to int)
    comparisons (< <= > >=)
    if, elif, else

Instructions

    Have the user enter a number representing the grade (0-100)
    Convert the number grade to a letter grade

Numeric Ranges

    90-100: A
    80-89: B
    70-79: C
    60-69: D
    0-59: F

'''
def grade(num):
    if num in range(90,101):
        print('Your grade = A')
    elif num in range(80,90):
        print('Your grade = B')
    elif num in range(70,80):
        print('Your grade = C')
    elif num in range(60,70):
        print('Your grade = D')
    else:
        print('Your grade = F')
    return num

(grade(50))