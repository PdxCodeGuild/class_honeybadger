# addition  function
def add (x, y):
    return x + y
# subtraction function
def subtract(x, y):
    return x - y
# multiplication function
def multiply (x, y):
    return x * y
# division function
def division (x, y):
    return x / y

print("Select operation")
print("1.Add")
print("2.Subtract")
print("3.Division")
print("4.Multiplication")

choice = input("Enter choice (1/2/3/4:)")
num1 = int(input("What is the first number?: "))
num2 = int(input("what is the second number?: "))

if choice == "1":
    print(num1, '+',num2,"=", add(num1,num2))

elif choice == "2":
    print(num1, "+",num2, "=", subtract(num1,num2))
elif choice == "3":
    print(num1, "+", num2, "=", division(num1,num2))
elif choice == "3":
    print(num1, "+", num2, "=", multiply(num1,num2))
    
