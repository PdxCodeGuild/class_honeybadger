'''
Lab 11: Simple Calculator

Let's write a simple REPL (read evaluate print loop) calculator that can handle addition, subtraction, multiplication, and division. 
Ask the user for an operator and each operand. Don't forget that input returns a string, which you can convert to a float using 
float(user_input) where user_input is the string you got from input. Below is some sample input/output.

> What is the operation you'd like to perform? +
> What is the first number? 5
> What is the second number? 12
> 5 + 12 = 17

Version 2

Allow the user to keep performing operations until they say 'done'. Use while True and break. Below is some sample input/output.

> what is the operation you'd like to perform? +
> what is the first number? 5
> what is the second number? 12
> 5 + 12 = 17
> what is the operation you'd like to perform? done
> goodbye! 

'''

def calc_num():
    mylist = []

    operation = input('What is the operation you would like to perform? ')
    number1 = float(input('What is the first number? '))
    number2 = float(input('What is the second number? '))

    mylist.append(number1)
    mylist.append(number2)
    print(mylist)

    if operation == '+':
        addition = mylist[0]+mylist[1]
        print(addition)
    elif operation == '*':
        multiplication = mylist[0]*mylist[1]
        print(multiplication)
    elif operation == '-':
        subtraction = mylist[0]-mylist[1]
        print(subtraction)
    elif operation == '/':
        division = mylist[0]/mylist[1]
        print(division)
    else:
        print('Please enter a valid operand (+, -, * or /)')
    
    
def calc_num2():
    mylist1 = []
    operation = input('What is the operation you would like to perform? ')
    
    while True:
        
        number = input('Enter a number? ')
        if number == 'done':
            break
        addition = 0
        subtraction = 0
        multiplication = 0
        division = 0
         
        mylist1.append(float(number))
              
        for i in range(len(mylist1)):
            
            if operation == '+':
                addition +=mylist1[i]
                print(f'The numbers to be added are {mylist1}')
                print(f'The sum of these numbers = {addition}')
            
            elif operation == '-':
                subtraction -=mylist1[i]
                print(f'The numbers to be subtracted are {mylist1}')
                print(f'The subtracted numbers = {subtraction}')


            elif operation == '*':
                multiplication *=mylist1[i]
                print(f'The numbers to be multiplied are {mylist1}')
                print(f'The multiplied numbers = {multiplication}')

            elif operation == '/':
                division /=mylist1[i]
                print(f'The numbers to be multiplied are {mylist1}')
                print(f'The multiplied numbers = {division}')

        #print(mylist)

        
calc_num()
# calc_num2() #---> subtraction/division not computing correctly. Addition/multiplication printing the previous total value

