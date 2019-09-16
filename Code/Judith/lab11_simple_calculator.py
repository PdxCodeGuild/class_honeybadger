#filename: simple_calculator.py
#vers2

operators = ["+", "-", "*", "/"]
num1 = 0
num2 = 0
product = 0
flag = True

def concat(num1, oper, num2):
    num1 = str(num1)
    num2 = str(num2)
    oper = str(oper)
    statement = num1 + oper + num2
    product = eval(statement)
    print(product)

while flag == True:
    oper = input("choose an operation (+, -, *, /)")
    num1 = float(input("Enter your first number"))
    num2 = float(input("Enter your second number"))
    concat(num1, oper, num2)
    
    yorn = input("would you like to perform another operation? y or n\n")
    if yorn == 'y':
        continue
    else:
        break

# Version 3 ###############################

# oper = str(input('give us a problem'))
# prod = eval(oper)
# print(prod)
    



   
