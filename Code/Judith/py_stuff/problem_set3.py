# #filename: problem_set3.py

import random

# # problem 1
# # Write a function using random.randint to generate an index, use that index to pick a random element of a list and return it.
# def randelem():
#     ulist = [1,2,3,4,5]
#     return ulist[random.randint(0,4)]
# #print(randelem())

# # problem 2
# # Write a REPL which asks users for a list of numbers, which they enter, until they say 'done'. Then print out the list.
# def listmkr():
#     lis = []
#     ad = ''
#     while ad != 'done':
#         ad = input('num pls...')
#         lis.append(ad)
#     lis.remove('done')
#     return lis
# #print(listmkr())

# # problem 3
# # Write a function that takes a list of numbers, and returns True if there is an even number of even numbers.
# def evtru():
#     lis = []
#     elis = []
#     for i in range(8):
#         lis.append(random.randint(0,10))
#     print(lis)
#     for i in range(len(lis)):
#         if lis[i]%2==0:
#             elis.append(lis[i])
#     print(elis)
#     if len(elis)%2==1:
#         return False
#     else:
#         return True            
# #print(evtru())

# # problem 4
# # Print out every other element of a list, first using a while loop, then using a for loop.
# def bkbt():
#     blis = []
#     flis = []
#     wlis = []
#     a = 0
#     for i in range(8):
#         blis.append(random.randint(0,99))
#     print(blis)
#     for i in range(len(blis)):
#         if i%2!=0:
#             flis.append(blis[i])
#     print(flis)
#     while a <= len(blis):
#         if index %2==0:
#             wlis.append(blis[index])
#             a += 2
#         else:
#             break        
#     print(wlis)
# print(bkbt())

# # problem 5
# # Write a function that returns the reverse of a list.

# # problem 6
# # Write a function to move all the elements of a list with value less than 10 to a new list and return it.
# def movelownums():
#     lis = []
#     elis = []
#     for i in range(8):
#         lis.append(random.randint(0,20))
#     for i in range(len(lis)):
#         if lis[i]<10:
#             elis.append(lis[i])
#     return elis
# print(movelownums())

# def movelownums2()
#     num = [random.randint(0,20) for i in range(10)]
#     elis = [num for num in num if num<10]
#     print(num)
#     return elis
# print(movelownums())

# # problem 7
# # Write a function to find all common elements between two lists.
# def comel():
#     lis = [random.randint(0,10) for i in range(10)]
#     elis = [random.randint(0,10) for i in range(len(lis))]
#     flis = []
#     for i in range(len(lis)):
#         if lis[i] == elis[i]:
#             flis.append(lis[i])
#     print(lis)
#     print(elis)
#     return int(len(flis))
# print(comel())

# # problem 8: 
# # combine two lists of equal length into one,alternating elements
# def combine():
#     list_one = [random.randint(0,99) for x in range(5)]
#     list_two = [random.randint(0,99) for x in range(5)]
#     list_three = []
#     print(list_one)
#     print(list_two)
#     for i in range(len(list_one)):
#         list_three.append(list_one[i])
#         list_three.append(list_two[i])
#     return list_three
# print(combine())

# # problem 9: 
# # Given a list of numbers, and a target number, find a pair of numbers from the list that sum to a target number
# def p9():
#     nums = [5,6,2,3]
#     target = 8
#     print('target is ', target)
#     pairs = []
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[j] + nums[i] == target:
#                  pairs.append([nums[i], nums[j]])
#     return pairs
            
# print(p9())

# # problem 10: 
# # Write a function that merges two lists into a single list, where each element of the output list is a list containing two elements, one from each of the input lists.
# def p10():
#     list_one = [random.randint(0,99) for x in range(5)]
#     list_two = [random.randint(0,99) for x in range(5)]
#     list_three = []
#     print(list_one)
#     print(list_two)
#     for i in range(len(list_one)):
#         list_three.append([list_one[i], list_two[i]])
#     return list_three
# print(p10())

# # problem 11: 
# # Write a function combine_all that takes a list of lists, and returns a list containing each element from each of the lists.
# def combine_all():
#     list_one = [[random.randint(0,99) for x in range(3)] for x in range(3)]
#     list_two = []
#     print(list_one)
#     for i in list_one:
#         for j in i:
#             list_two.append(j)
#     return list_two
# print(combine_all())

# # problem 12: 
# # Write a function that takes n as a parameter, and returns a list containing the first n Fibonacci Numbers.
# def p12(n):
#     list_two = [1,1]
#     for x in range(len(list_two),n):
#         list_two.append(list_two[x-1]+list_two[x-2])
#     return list_two
# print(p12(12))

# # problem 13: 
# # Write functions to find the minimum, maximum, mean, and (optionally) mode of a list of numbers.
# def minimum(nums):
#     mini = nums[0]
#     for num in nums:
#         if num < mini:
#             mini = num
#     return mini

# def maximum(nums):
#     max = nums[0]
#     for num in nums:
#         if num > max:
#             max = num
#     return max
        
# def mean(nums):
#     return sum(nums) / len(nums)

# def mode(nums):
#     current_mode = 0
#     scount = 0
#     for i in range(len(nums)):
#         count = 0
#         for num in nums:
#             if num == nums[i]:
#                 count += 1
#         if count > scount:
#             scount = count
#             current_mode = nums[i] 
                
#     return current_mode

# nums = [0, 3, 3, 6, 9, 9, 9]
# print(minimum(nums), maximum(nums), mean(nums), mode(nums))
        
# # problem 14: 
# # Write a function which takes a list as a parameter and returns a new list with any duplicates removed.
# def p14(nums):
#     no_dupes = []
#     for i in range(len(nums)):
#         if nums[i] not in no_dupes:
#             no_dupes.append(nums[i])
#     return no_dupes

# nums = [0, 1, 1, 2, 3, 4, 4, 6]
# print(p14(nums))


    

