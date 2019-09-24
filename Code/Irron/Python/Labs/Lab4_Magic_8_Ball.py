'''
Lab 4: Magic 8-Ball

Let's write a program to simulate the classic "Magic Eight Ball"
Concepts Covered

    input, print
    import
    random.choice

Instructions

    Print a welcome screen to the user.
    Use the random module's random.choice() to choose a prediction.
    Prompt the user to ask the 8-ball a question "will I win the lottery tomorrow?"
    Display the result of the 8-ball.
'''

import random

def magic8(predictions):
    #mylist = []
    predict_split = predictions.split(',')
    #print(predict_split)
    random_respone = random.choice(predict_split)
    #print(random_respone)
    
    return random_respone


S = '''
It is certain,
It is decidedly so,
Without a doubt,
Yes definitely,
Most likely,
Outlook good,
Yes,
Signs point to yes,
Ask again later,
Cannot predict now,
Don't count on it,
My reply is no,
My sources say no,
Outlook not so good,
Very doubtful,
Hell No!!
    
    '''

user_input = input('Please enter an 8-Ball question ')    
print(magic8(S))


