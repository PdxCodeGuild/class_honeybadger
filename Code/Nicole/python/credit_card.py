# credit_card.py

# Convert the input string into a list of ints
# Slice off the last digit. That is the check digit.
# Reverse the digits.
# Double every other element in the reversed list.
# -- Subtract nine from numbers over nine.
# -- Sum all values.
# -- Take the second digit of that sum.
# -- If that matches the check digit, the whole card number is valid.

def credit_card():
    cc = True
    while cc is True:
        user_cc = input("\nPlease enter your credit card number: ")
        user_cc = list(map(int, user_cc))
        if len(user_cc) != 16:
            print("\nYou did not enter a valid credit card number (16 digits).")
        print(*user_cc)
        
        user_cc_check = user_cc[15:16]
        print(*user_cc_check)
        
        user_cc_reverse = user_cc[0:15]
        print(*user_cc_reverse)
        
        user_cc_reverse = user_cc_reverse[::-1]
        print(*user_cc_reverse)
        
        for i in range(0, len(user_cc_reverse), 2):
            user_cc_reverse[i] *= 2
        user_cc_double = user_cc_reverse
        print(*user_cc_double)
        
        for i in range(len(user_cc_double)):
            if user_cc_double[i] > 9:
                user_cc_double[i] -= 9
        user_cc_minus = user_cc_double
        print(*user_cc_minus)
        
        total = 0
        for i in range(len(user_cc_minus)):
            total += user_cc_minus[i]
        
        print(total)
        
        total = str(total)
        total = list(total)
        total = total[1:2]
        
        print(*total)
        
        total = list(map(int, total))
        
        if user_cc_check == total:
            print("Success! Your credit card number is valid.")
        else:
            print("Your credit card is NOT valid.")
        
        cc = False
        # if user_numbers 

print(credit_card())

# 4556737586899855