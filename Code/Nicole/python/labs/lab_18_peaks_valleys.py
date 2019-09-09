# peaks_valleys.py

def peaks(nums):
    peaks_list = []
    # for i in range(1, 19):
    for i in range(1, len(nums)-1):
        if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            peaks_list.append(i)
    return peaks_list
    
def valleys(nums):
    valleys_list = []
    for i in range(1, len(nums)-1):
        if nums[i] < nums[i - 1] and nums[i] < nums[i + 1]:
            valleys_list.append(i)
    return valleys_list

def peaks_and_valleys(nums):
    list_1 = peaks(nums)
    list_2 = valleys(nums)
    sorted_list = []
    for x in range(len(list_1)):
        sorted_list.append(list_1[x])
    for y in range(len(list_2)):
        sorted_list.append(list_2[y])
    sorted_list = sorted(sorted_list)
    return sorted_list

def created_chart(nums):
    rows = []
    for i in range(1, 10):
        sub_row = []
        for x in range(len(nums)):
            if nums[x] >= i:
                sub_row.append("X")
            else:
                sub_row.append(" ")
        rows.append(sub_row)
    # this reverses the rows of rows so it displays properly
    rows = rows[::-1]
    # this prints the lists pretty
    for index in range(len(rows)):
        print(*rows[index])
        index += 1
    print(*nums)
    
    
    # for i in range(9):
    #     rows.append([i])
    #     for x in range(len(nums)):
    #         if nums[x] == i:
    #             rows[0].append('X')
    # print(*rows)
    
    # rows[0].append('X')
    
# def created_chart(nums):
#     row_1 = [] 
#     row_2 = []
#     row_3 = [] 
#     row_4 = []
#     row_5 = []
#     row_6 = []
#     row_7 = []
#     row_8 = []
#     row_9 = []
#     numbers = list(nums)
#     for x in range(len(numbers)):
#         if numbers[x] == 1:
#             row_1.append("X")
#             row_2.append(" ")
#             row_3.append(" ")
#             row_4.append(" ")
#             row_5.append(" ")
#             row_6.append(" ")
#             row_7.append(" ")
#             row_8.append(" ")
#             row_9.append(" ")
#         if numbers[x] == 2:
#             row_1.append("X")
#             row_2.append("X")
#             row_3.append(" ")
#             row_4.append(" ")
#             row_5.append(" ")
#             row_6.append(" ")
#             row_7.append(" ")
#             row_8.append(" ")
#             row_9.append(" ")
#         if numbers[x] == 3:
#             row_1.append("X")
#             row_2.append("X")
#             row_3.append("X")
#             row_4.append(" ")
#             row_5.append(" ")
#             row_6.append(" ")
#             row_7.append(" ")
#             row_8.append(" ")
#             row_9.append(" ")
#         if numbers[x] == 4:
#             row_1.append("X")
#             row_2.append("X")
#             row_3.append("X")
#             row_4.append("X")
#             row_5.append(" ")
#             row_6.append(" ")
#             row_7.append(" ")
#             row_8.append(" ")
#             row_9.append(" ")
#         if numbers[x] == 5:
#             row_1.append("X")
#             row_2.append("X")
#             row_3.append("X")
#             row_4.append("X")
#             row_5.append("X")
#             row_6.append(" ")
#             row_7.append(" ")
#             row_8.append(" ")
#             row_9.append(" ")
#         if numbers[x] == 6:
#             row_1.append("X")
#             row_2.append("X")
#             row_3.append("X")
#             row_4.append("X")
#             row_5.append("X")
#             row_6.append("X")
#             row_7.append(" ")
#             row_8.append(" ")
#             row_9.append(" ")
#         if numbers[x] == 7:
#             row_1.append("X")
#             row_2.append("X")
#             row_3.append("X")
#             row_4.append("X")
#             row_5.append("X")
#             row_6.append("X")
#             row_7.append("X")
#             row_8.append(" ")
#             row_9.append(" ")
#         if numbers[x] == 8:
#             row_1.append("X")
#             row_2.append("X")
#             row_3.append("X")
#             row_4.append("X")
#             row_5.append("X")
#             row_6.append("X")
#             row_7.append("X")
#             row_8.append("X")
#             row_9.append(" ")
#         if numbers[x] == 9:
#             row_1.append("X")
#             row_2.append("X")
#             row_3.append("X")
#             row_4.append("X")
#             row_5.append("X")
#             row_6.append("X")
#             row_7.append("X")
#             row_8.append("X")
#             row_9.append("X")
#     print(*row_9)
#     print(*row_8)
#     print(*row_7)
#     print(*row_6)
#     print(*row_5)
#     print(*row_4)
#     print(*row_3)
#     print(*row_2)
#     print(*row_1)
#     print(*numbers)


data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

print(peaks(data))
print(valleys(data))
print(peaks_and_valleys(data))
print(created_chart(data))