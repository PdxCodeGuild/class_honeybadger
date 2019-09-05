# practice_3_lists_prob4.py

number_list = ["tree", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
even_odd_list = []
index = 0

while index <= len(number_list):
    if index % 2 == 0:
        even_odd_list.append(number_list[index])
    else:
        break
    index += 2

# for i in range(len(number_list)):
#     if i % 2 == 0:
#         even_odd_list.append(number_list[index])
#     else:
#         continue
#     index += 2

print(even_odd_list)