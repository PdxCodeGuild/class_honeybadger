# time_to_phrase.py

# not finished

def time_to_phrase(clock_hours, clock_mins):
    hours = {
        1: "one", 
        2: "two", 
        3: "three", 
        4: "four", 
        5: "five", 
        6: "six", 
        7: "seven", 
        8: "eight", 
        9: "nine", 
        10: "ten",
        11: "eleven",
        12: "twelve"
        }
    min_ones = {
        1: "one", 
        2: "two", 
        3: "three", 
        4: "four", 
        5: "five", 
        6: "six", 
        7: "seven", 
        8: "eight", 
        9: "nine", 
        10: "ten"
        }
    min_teens = {
        1: "eleven", 
        2: "twelve", 
        3: "thirteen", 
        4: "fourteen", 
        5: "fifteen", 
        6: "sixteen", 
        7: "seventeen", 
        8: "eighteen", 
        9: "nineteen"
        }
    min_tens = {
        2: "twenty", 
        3: "thirty", 
        4: "forty", 
        5: "fifty", 
        6: "sixty", 
        7: "seventy", 
        8: "eighty", 
        9: "ninety"
        }
    min_speech = {
        10: "ten past ",
        15: "a quarter past ",
        20: "twenty past ",
        30: "half past ",
        40: "twenty to ",
        45: "a quarter to ",
        50: "ten to "
    }

    # determine the current time
    # use that

    time_phrase = "The current time is "

    # time = ""
    # time += clock_hours
    
    # clock mins = 10, 15, 20, 30, 40, 45, 50
    if clock_mins in min_speech:
        pass
        if clock_mins > 40:
            clock_hours += 1
            if clock_hours == 13:
                clock_hours = 1
        time_phrase += min_speech[clock_mins] + str(clock_hours)

    # if clock_mins <= 10:
    #     time +=
    # elif clock_mins > 10 and clock_mins < 20:
    #     pass



    return time_phrase



user_time_hour = int(input("What is the hour? "))
user_time_minutes = int(input("What are the minutes? "))
print(time_to_phrase(user_time_hour, user_time_minutes))