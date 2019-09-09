# practice_3_lists_prob3.py

# I need to redo this to make it an "even number of even numbers"

# define function

num_list =[]

def even_or_odd(a):
    if len(a) % 2 == 0:
        even = "Your list has an even number of items"
    else:
        even = "Your list does NOT have an even number of items"
    return even

while True:
    user_num = input("Please enter a number (or type \"done\" if finished): ")
    if user_num == "done" or user_num == "":
        break
    num_list.append(user_num)
    
print(f"Your list contains {len(num_list)} items.")
print(even_or_odd(num_list))