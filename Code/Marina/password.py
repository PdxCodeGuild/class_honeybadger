import random
import string

lttrs = string.ascii_lowercase + string.ascii_uppercase
nums = string.digits
dots = string.punctuation

options = lttrs + nums + dots

answer = input("How long would you like your password to be? ")

your_password = ""

for x in range (int(answer)):
    your_password += random.choice(options)

print(f"Your {answer} character password is: {your_password}")
