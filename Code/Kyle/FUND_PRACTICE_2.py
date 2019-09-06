num1 = int(input("Please enter a number "))
num2 = int(input("Please enter another number "))

def pos_odd(num1, num2):
    
    if num1 > 0 and num2 < 0:
        print("True")
    elif num1 < 0 and num2 > 0:
        print("True")
    else:
        print("False")


pos_odd(num1, num2)
        
