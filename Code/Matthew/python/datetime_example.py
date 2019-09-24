


import datetime


def pretty_print(date):
    
    day_suffix = ''
    
    ones_digit = date.day%10
    tens_digit = date.day//10
    if tens_digit == 1:
        day_suffix = 'th'
    else:
        if ones_digit == 1:
            day_suffix = 'st'
        elif ones_digit == 2:
            day_suffix = 'nd'
        elif ones_digit == 3:
            day_suffix = 'rd'
        else:
            day_suffix = 'th'

    day = int(date.strftime('%d'))
    return date.strftime(f'%A, %B {day}{day_suffix} %Y')



# date = datetime.datetime.now()
date = datetime.datetime(2019, 9, 1)
for i in range(40):
    print(pretty_print(date))
    dt = datetime.timedelta(days=1)
    date += dt
    
    
    



