# avg_nums_v2.py

# Ask the user to enter the numbers one at a time, putting them into a list.
# If the user enters 'done', then calculate and display the average.

import sys

# define number list

print("*" * 10 + "\n")
print("Welcome to the 'number averag-ator'. You will be asked to enter numbers below. When you are finished, type \"done\" and the numbers you entered will be averaged.\n")

nums = []

while True:
    user_nums = input("Please enter a number: ")
    if user_nums.isdigit():
        user_nums = int(user_nums)
        nums.append(user_nums)
        continue
    elif user_nums == "done":
        break
    else:
        print("You did not enter a number. Please start over.\n")
        sys.exit()

# print(nums)

running_sum = 0

for num in range(len(nums)):
    running_sum += nums[num]

avg_sum = running_sum / len(nums)
print(f"\nYour average number is: {avg_sum}")
