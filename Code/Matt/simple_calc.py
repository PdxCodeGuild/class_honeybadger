def calc():
    operator = input('choose an operation\(+ , - , * , /) OR "done" if your finished ')
    game_in_session = "+"
    while game_in_session:

        a = int(input('Enter your first number: '))
        b = int(input('Enter your second number: '))

        if operator == '+':
            x = a + b
            print(x)
        elif operator == '-':
            x = a - b
            print(x)
        elif operator == '*':
            x = a * b
            print(x)
        elif operator == '/':
            x = a / b
            print(x)

    break 
calc()
