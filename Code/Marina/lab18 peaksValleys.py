# peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.
#
# valleys - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.
#
# peaks_and_valleys - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.

data_list = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(data_list):
    peaks_list = []
    for i in range(1,len(data_list)-1):
        if data_list[i] > data_list[i-1] and data_list[i] > data_list[i+1]:
            peaks_list.append(i)
    return peaks_list

print(peaks(data_list))

def valleys(data_list):
    valleys_list = []
    for i in range(1, len(data_list)-1):
        if data_list[i] < data_list[i-1] and data_list[i] < data_list[i+1]:
            valleys_list.append(i)
    return valleys_list

print(valleys(data_list))

def peaks_and_valleys(data_list):
    both = []
    sorted_list = []
    both = peaks(data_list) + valleys(data_list)
    print(both)
    sorted_list = sorted(both)
    return sorted_list
print(peaks_and_valleys(data_list))

def draw(data_list):
    for num in data_list:
        print('X' * num)
#     for i in range(len(data_list)):
#         print('X' * data_list(i))
draw(data_list)
