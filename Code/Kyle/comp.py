
input_list = []

while True:
    if user_input == "done": break
    user_input = input("enter a number or type done: ")
    input_list.append(int(user_input))

print(input_list)
