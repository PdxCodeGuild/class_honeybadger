# practice_3_lists_prob2.py

# define list

num_list = []

while True:
    user_num = input("Please enter a number (or \"done\" if finished): ")
    if user_num == "done":
        break
    num_list.append(user_num)

print(num_list)