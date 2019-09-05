# simple_calculator.py

# Let's write a simple REPL (read evaluate print loop) calculator that can handle addition, subtraction, multiplication, and division.
# Ask the user for an operator and each operand. Don't forget that input returns a string, which you can convert to a float using float(user_input) where user_input is the string you got from input. Below is some sample input/output.

import sys

def operator(num1, num2):
    if user_operation == "+":
        calculation = num1 + num2
        return calculation
    if user_operation == "-":
        calcluation = num1 - num2
        return calculation
    if user_operation == "*":
        calculation = num1 * num2
        return calculation
    if user_operation == "/":
        calculation = num1 / num2
        return calculation

operator_list = ["+", "-", "*", "/"]

while True:
    user_operation = input("\nWhat is the operation you would like to perform? Type \"done\" if you are finished.\n")
    if user_operation in operator_list:
        pass
    elif user_operation == "done":
        break
    else:
        print("\nYou did not enter a correct operator value. Please start over and try again.\n")
        sys.exit()
    user_num1 = input("What is the first number?")
    user_num1 = float(user_num1)
    user_num2 = input("What is the second number?")
    user_num2 = float(user_num2)
    calculation = operator(user_num1, user_num2)
    print(f"Your calculation is {calculation}")
