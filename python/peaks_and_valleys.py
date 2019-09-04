





def peaks(data):
    r = []
    for i in range(1, len(data)-1):
        # if i == 0 or i == len(data)-1:
        #     continue
        # print(i-1, data[i-1])
        # print(i, data[i])
        # print(i+1, data[i+1])
        # print()
        # if data[i-1] < data[i] > data[i+1]:
        if data[i] > data[i+1] and data[i] > data[i-1]:
            r.append(i)
    return r
            

def valleys(data):
    r = []
    for i in range(1, len(data)-1):
        # if i == 0 or i == len(data)-1:
        #     continue
        # print(i-1, data[i-1])
        # print(i, data[i])
        # print(i+1, data[i+1])
        # print()
        if data[i] < data[i+1] and data[i] < data[i-1]:
            r.append(i)
    return r


def peaks_and_valleys(data):
    p = peaks(data)
    v = valleys(data)
    r = p + v
    r.sort()
    return r


data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
print(peaks(data))
print(valleys(data))
print(peaks_and_valleys(data))


# for num in data:
#     print('x'*num)

# for num in data:
#     for i in range(num):
#         print('x', end='')
#     print()



# for i in range(10):
#     for j in range(5):
#         print(i, j)
# 


# 
# s = ''
# for i in range(max(data), 0, -1):
#     for j in range(len(data)):
#         # s += ' ' if data[j] < i else 'X'
#         if data[j] < i:
#             s += ' '
#         else:
#             s += 'X'
#     s += '\n'
# 
# print(s)








