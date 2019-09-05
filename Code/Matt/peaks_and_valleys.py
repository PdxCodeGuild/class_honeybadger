#peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.

#valleys - Returns the indices of 'valleys'. A valley is a number with a higher number on #both the left and the right.

#peaks_and_valleys - uses the above two functions to compile a single list of the peaks and #valleys in order of appearance in the original data.

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks_check(data):
    peaks = []
    for i in range(1, len(data)-1):
         if data[i] > data[i + 1]  and data[i] > data[i - 1]:
             peaks.append(i)
    return peaks

def valleys_check(data):
    valleys = []
    for i in range(1, len(data)-1):
         if data[i] < data[i +1] and data[i] < data[i -1]:
             valleys.append(i)
    return valleys

def list_combiner():
    new_list=[]
    new_list.append()
    new_list.append()
    print (new_list)

print(peaks_check(data))
