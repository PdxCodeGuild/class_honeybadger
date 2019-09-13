# filename: calculator.py
# learning objective: if/elif/else statements

# MVP - most viable product
# print welcome msg - d
# allow the user to enter two numbers - d
# allow the computer to randomly choose an operator
# print results using a conditional statement

# Stretch
# allow to pay again
# keep track of their "score"

import random

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a second number: "))

operators_list = ["+", "-", "*", "/"]

chosen_operator = input("Enter an operator ")

print(chosen_operator)


# if/else = 2 conditions
# elif = more than 2 conditions

if chosen_operator == "+":
    results = num1 + num2
elif chosen_operator == "-":
    results = num1 - num2
elif chosen_operator == "*":
    results = num1 * num2
else:
    results = num1 / num2

print(results)
