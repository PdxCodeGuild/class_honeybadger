#Obtaining user info
operator1 = float(input("Please enter the 1st number"))
operator2 = float(input("Please enter the 2nd number"))
operand = input("Please enter +, -, / or * ")

if operand == "+":
    addition = operator1+operator2
    print(addition)
elif operand == "-":
    subtraction = operator1-operator2
    print(subtraction)
elif operand == "/":
    division = operator1/operator2
    print(division)
else:
    multiplication = operator1*operator2
    print(multiplication)


