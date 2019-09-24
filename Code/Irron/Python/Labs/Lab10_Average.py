'''
Lab 10: Average Numbers

We're going to average a list of numbers. Start with the following list, iterate through it, keeping a 'running sum', 
then divide that sum by the number of elements in that list. Remember len will give you the length of a list.

The code below hows how to loop through an array, and prints the elements one at a time.

nums = [5, 0, 8, 3, 4, 1, 6]

# loop over the elements
for num in nums:
    print(num)

# loop over the indices
for i in range(len(nums)):
    print(nums[i])

Version 2

Ask the user to enter the numbers one at a time, putting them into a list. If the user enters 'done', then calculate and display 
the average. The following code demonstrates how to add an element to the end of a list.

nums = []
nums.append(5)
print(nums)

Below is an example input/output:

> enter a number, or 'done': 5
> enter a number, or 'done': 3
> enter a number, or 'done': 4
> enter a number, or 'done': done
average: 4


Version 3

Calculate the median. The median is the number in the middle when the list is sorted. If there's an even number of numbers, 
the median is a list of the two numbers in the middle. Remember the sort method on lists.


Version 4 (optional)

The mode is the number that occurs the most. There may be multiple modes. Hint: use a dictionary to count the occurances of each number, 
the key can be the number, the value can be the number of occurances. If it's not in the dictionary, add it and set it's value to one. 
If it's already in the dictionary, increment that value.

counts = list(word_dict.items()) # .items() returns a list of tuples
counts.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
print(counts)

'''
##      0  1  2  3  4  5  6
# nums = [5, 0, 8, 3, 4, 1, 6]

#loop over indicies to #iterate thru list, keep track of running total, compute average
# sum = 0
# for i in range(len(nums)):
#     sum +=nums[i] # variable where I want to hold the accumulating total goes on the right, variable I am accumulating goes on the left
#     average = sum/len(nums)
# print(sum)
# print(average)


#Part2 ---> ask user to inpu numbers, add numbers to a list. When user types 'done', calculate and display the average.

def calc_average():
    numbers = []
    while True:
        total = 0  #---> needed to create starting value for equation total = total + numbers in the list. Needs to be inside loop, if outside loop, will retain value of lastes number and add to total
        nums = input('Please enter a number. When finished, type done ')
        if nums == 'done':
            break
        numbers.append(float(nums)) #---> taking input and appending to a list as an integer, needed for math operations
        for i in range(len(numbers)): #---> need to loop over the indicies in order to assing the value at the index to iterating variable i.  In essence, iterate to index 0, assign the value at index 0 to iterative i. This i value will can be used to accumulate totals 
            total +=numbers[i] #---> iterates thru loop of numbers in list, assigns each value to i, accumulates value and assings to variable total
          
        sorts = sorted(numbers) #--->sorting list and assigning to variable sorts
        average = round(total/len(numbers))

        print(f'Numbers entered = {numbers}')
        print(f'Running total of numbers = {total}')
        print(f'Sorted numbers = {sorts}')
        print(f'The average = {average}')
    return sorts
            
    
def compute_median(sortlist): #---> passing the sorted list from the calc_average function
    mylist = sortlist #---> was testing with mylist, so pointed the sorted list from calc_average to mylist.
    #mylist = [1,2,3,4,5,8]
    if len(mylist)%2 == 0:
        middlea = mylist[len(mylist)//2-1] #---> -1 shifts 1 to left. floor division gets rid of remainder and returns whole number, so 3//2 = 1, not 1.5
        middleb = mylist[len(mylist)//2]
        print(f'An even # of numbers entered. In this case, the median = {middlea}, {middleb}')
    else:
        middle = mylist[len(mylist)//2]
        print(f'The medain = {middle}')
    
    #print(mylist)
            

sorts = calc_average() #---> calling the results of the calc_average function and assigning value to variable sorts. calc_average will return a list of sorted numbers user entered 
compute_median(sorts)  #---> calling function and passing sorts, which is results of calc_average function


##Misc Code

##loop over elements
# for num in nums:
#     print(num)










