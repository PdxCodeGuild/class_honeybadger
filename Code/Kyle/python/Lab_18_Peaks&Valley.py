def peaks(data):
    peak = []
    for i in range(1, len(data)-1):
        if data[i] > data[i+1] and data[i] > data[i-1]:
            peak.append(i)
    return peak


def valley(data):

    valley = []
    for i in range(len(data)-1):
        if data[i] < data[i+1] and data[i] < data[i-1]:
            valley.append(i)
    return valley


# def peak_and_valley(data):
#     peak_valley = []
#     peak_valley = peaks + valley


data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

# print(peaks(data))
# print(valley(data))

print(peaks(data))
print(valley(data))
