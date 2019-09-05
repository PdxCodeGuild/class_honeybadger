
user_num = int(input('Enter a number: '))
def num_to_word(user_num):
    tens_digit = user_num // 10
    ones_digit = user_num % 10
    # print(f'{tens_digit}{ones_digit}')
    hundreds_digit = user_num // 10
    hundreds_digit2 = hundreds_digit // 10


    ones_mapping = {
        1: "one",
        2: "two",
        3:"three",
        4:"four",
        5:"five",
        6:"six",
        7:"seven",
        8:"eight",
        9:"nine",
        10:"ten",
        11:"eleven",
        12:"twelve",
        13:"thirteen",
        14:"fourteen",
        15:"fifteen",
        16:"sixteen",
        17:"seventeen",
        18:"eighteen",
        19:"nineteen",
    }

    tens_mapping = {
        2:"twentey",
        3:"thirty",
        4:"forty",
        5:"fiffty",
        6:"sixty",
        7:"seventy",
        8:"eighty",
        9:"ninety",
    }

    hundreds_mapping = {
        1:"one hundrend",
        2:"two hundrend",
        3:"three hundrend",
        4:"four hundrend",
        5:"five hundrend",
        6:"six hundrend",
        7:"seven hundrend",
        8:"eight hundrend",
        9:"nine hundrend",
    }




    if user_num <= 19:
        print(ones_mapping[user_num])
    if user_num >= 19 and user_num <= 99:
        print(tens_mapping[tens_digit]+ " " + ones_mapping[ones_digit])
    if user_num >= 100:
        print(hundreds_mapping[hundreds_digit2])





num_to_word(user_num)
