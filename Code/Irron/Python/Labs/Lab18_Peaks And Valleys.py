''' Lab 18: Peaks and Valleys

Define the following functions:

    peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.

    valleys - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.

    peaks_and_valleys - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in 
    the original data.

Visualization of test data:
Data 	1 	2 	3 	4 	5 	6 	7 	6 	5 	4 	5 	6 	7 	8 	9 	8 	7 	6 	7 	8 	9
Index 	0 	1 	2 	3 	4 	5 	6 	7 	8 	9 	10 	11 	12 	13 	14 	15 	16 	17 	18 	19 	20
POI 							P 			V 					P 			V 			

Example I/O:

                                                      X                 X
                                                   X  X  X           X  X
                              X                 X  X  X  X  X     X  X  X
                           X  X  X           X  X  X  X  X  X  X  X  X  X
                        X  X  X  X  X     X  X  X  X  X  X  X  X  X  X  X
                     X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
                  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
               X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
            X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X

>>> data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
>>> peaks(data)
[6, 14]
>>> valleys(data)
[9, 17]
>>> peaks_and_valleys(data)
[6, 9, 14, 17] 
'''

def peaks(data):
    print (data)
    peaks = []

    for i in range(1, len(data)-1):#---> starting loop at position 1 and stopping loop at second to last position of dataset. 1 and -1 needed to ensure loops stay within range
        #print(i)      #---> Returns/prints the index of each element in list
        #print(data[i]) #---> Returns/prints the value associated with the index i
        #print(i, data[i]) #prints in columns

        if i == 0 or i == len(data)-1: #---> compares i to 0 or each variables index to ensure we stay within the loop.  
            continue #will pass over values that meet requirements in if statement. when i=0, data[i-1] will return negative1, which is out of range. and len(data)-1 will put data[i+1] or data[21] out of range because there is not a metric/value at index 21.
        #print(i-1, data[i-1]) #since the range begins with 1, the first index will = 0, and the first value from list will from index 1. The elements in list aligns to their respective index
        #print(i, data[i]) #begins with i = index 1, value of element = 2, which is 2nd number in list
        #print(i+1, data[i+1]) #begins with index =2 and value of element = 3
        print()
        if data[i]> data[i+1] and data[i]> data[i-1]:  #---> this compares current data[i] to positions on its immediate left and right. alternative syntax  data[i-1] <data[i]> data[i+1]
            peaks.append(data[i]) #appending the value of index that meets the if criteria
        #print(peaks)
    return peaks

def valleys(data):
    valleys = []
    
    for i in range(1, len(data)-1):
        if i == 0 or i == len(data)-1:
            continue
        if data[i] <data[i-1] and data[i] < data[i+1]:
            valleys.append(data[i])
        #print(valleys)
    return valleys

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
peaks = (peaks(data))
#print(peaks)

valleys= valleys(data)
#print(valleys)

print(f'The peaks are {peaks}. The valleys are {valleys}.')


''' Version 2 (optional)  Using the data list above, draw the image of X's above.'''
#data1 = [1, 2, 1,2] #----> created new list to test understanding of nested loop
for num in data: #---> nested loop which begins by assigning each variable in list num.   
    for i in range(num): #---> step 2, begins to iterate on num.  assigns each num index i, and the len of the range defined by value of num. 
        print('x', end='')  #---> num determines how many x's will be printed for each item in list. 1 will be printed once, 2 will be printed twice
    print()

# #example that shows how nested if statements work    
# for i in range(10): #---> creates a range of numbers (0 to 9)
#     for j in range(5): #---> index j is created and will instruct i to iterate 5 times.  
#         print(i, j) #---> each i will print 5 times


''' Version 3 (optional)

Make a function that takes in the dataset and a list of peaks, and returns a list of tuples representing lakes. 
Each tuple should have a starting x coordinate, an ending x coordinate, and a height. The height is relative to the base 
of the graph. '''

s = ''
#passing 3 parameters; lower & upper bounds, and increment. The max = the largest number in list, -1 will begin iteration at the last position of the list, so will start backwards, the 0 will = lowest number
for i in range(max(data), 0, -1):
    for j in range(len(data)): #---> creating another index for purpose of comparing i and j. j = the length of the list
        # s += ' ' if data[j] < i else 'X'
        if data[j] < i: #---> compares the actual value in the list to its index 
            s += ' ' #---> if so, add a blank to s
        else:
            s += 'X' #---> if not, add an X to s
    s += '\n' #---> believe this is a way of printing X to the next line??

print(s)

#code to understand how i and j are interacting. 
#i = the range of variables. 
#the max number is 9, and -1 will start at the the last number in list and 0 indidcates the count to stop interating
#so i in range(max(data), 0, -1) will return 9, 8, 7,.... and stop at 1
#for j in range(len(data)) = when at i , say number 9, print 9 times the length of the list 

#data[j] = returns the actual number at an index 
for i in range(max(data), 0, -1):
    for j in range(len(data)):
        #print (i, j)
        print(data[j], i)
        


''' Version 4 (optional)

Imagine pouring water into onto these hills. The water would wash off the left and right sides, but would accumulate in the 
valleys. Below the water is represented by O's. Given data, calculate the amount of water that would be collected.


                                                  X  O  O  O  O  O  X
                                               X  X  X  O  O  O  X  X
                          X  O  O  O  O  O  X  X  X  X  X  O  X  X  X
                       X  X  X  O  O  O  X  X  X  X  X  X  X  X  X  X
                    X  X  X  X  X  O  X  X  X  X  X  X  X  X  X  X  X
                 X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
              X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
           X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
        X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

'''
