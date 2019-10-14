# peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.
#
# valleys - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.
#
# peaks_and_valleys - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.
#
# data_list = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]


import random

# find the indices of the peaks(nums higher then their neighbors)
def peaks(data):
    peaks_indices = []
    # loop through list, avoiding the end points
    for i in range(1,len(data)-1):
        left = data [i-1]
        middle = data[i]
        right = data[i+1]
        if left < middle and right < middle:
            peaks_indices.append(i)
    return peaks_indices


# find the indices of the valleys
def valleys(data):
    valleys_indices = []
    for i in range(1, len(data)-1):
        left = data [i-1]
        middle = data[i]
        right = data[i+1]
        if left > middle and right > middle:
            valleys_indices.append(i)
    return valleys_indices

# draw
def draw(data):
    largest = max(data)
    for i in range(largest, 0, -1):
        row = ''
        for j in range(len(data)):
            if i <= data[j]:
                row += 'X'
            else:
                row += ' '
        print(row)


def let_it_rain(x):
    r = 0
    for j in range(max(x)):
        i = 0
        while i < len(x) and x[i] < j:
            i += 1
        while i < len(x):
            if x[i] < j:
                i0 = i
                while i < len(x) and x[i] < j:
                    i += 1
                if i == len(x):
                    break
                else:
                    r += i - i0 + 1
    return r

def main():
    data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

    draw(data)

    data = []
    for i in range(20):
        data.append(random.randint(1, 10))

    draw(data)

    print()
    print()

    data = []
    current_value = 5
    direction = random.choice([-1, 1])
    for i in range(20):
        data.append(current_value)
        current_value += direction
        if current_value < 1:
            current_value = 1
            direction = 1
        else:
            if random.random() < 0.2:
                direction = random.choice([-1, 1])
    draw(data)

main()
