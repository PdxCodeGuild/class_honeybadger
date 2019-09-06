


num1 = int(input("Please enter a number "))
num2 = int(input("A second number "))
num3 = int(input("A third number "))
num = []


 #used max() method to take maximum number in set and print it.
def highest_number(num):
    num_set = [num1, num2, num3]
    print(max(num_set))

highest_number(num)