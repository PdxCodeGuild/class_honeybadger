import random

# Problem #2

def random_element(a):
    return a[random.randint(0,len(a)-1)]
     
# fruits = ['apples', 'bananas', 'pears']
# print(random_element(fruits))

def repl():
    user_list = []
    while True:
        user_input = input("Please type a number. When you are finished, type 'done'. ")
        if user_input == "done":
            return user_list
        try:
            user_input = int(user_input)
            user_list.append(user_input)
        except ValueError:
            print("Please enter a valid value. :P ")
            
# print(*repl())

def even_even(nums):
    count = 0
    for num in nums:
        if num % 2 == 0:
            count += 1
    return count % 2 == 0
    
# print(even_even([5, 6, 2])) # True
# print(even_even([5, 5, 2])) # False

# def print_every_other(nums, end = " "):
#     index = 0
#     while index < len(nums):
#         print(nums[index], end = end)
#         index += 2




# for i in range(10):
#     print(i)
#     i += 10
#     print(i)
#     print()



def print_every_other(nums, end = " "):
    for i in range(0, len(nums), 2):
        print(nums[i], end = end)
    
 
# nums = [0, 1, 2, 3, 4, 5, 6, 7, 0, 2, 5, 7, 8]
# print_every_other(nums)
# # 0, 2, 4, 6, 8



# x = int(input('enter a number: '))
# # if x >= 0 and x <= 10
# if 0 <= x <= 10:
#     print('x is between 0 and 10')
# a = 5
# b = 5
# c = 5
# if a == b and b == c
# if a == b == c:






# def print(*args, sep=' ', end='\n'):
#     pass

# print('hello', 'world', '!', sep='_', end)

# greeting = random.choice(['it\'s so great you\'re here!', 'welcome', 'hello!'])
# print('mike' + ' ' + greeting)



# print('Here are your numbers: ', end='')
# for i in range(10):
#     print(i, end=' ')


# nums = [1, 2, 3, 4]
# print(nums, sep='_')
# print(*nums, sep='_') # print(1, 2, 3, 4, sep='_')


# def add(*nums):
#     r = 0
#     for num in nums:
#         r += num
#     return r
# nums = [5, 6, 7, 8]
# print(add(5, 6, 2))
# print(add(5, 6, 2, 3, 9))
# print(add(*nums))




# def example(nums):
#     nums.append(5)
# 
# 
# nums = [1, 2, 3, 4]
# example(nums)
# print(nums)




# x = 5
# y = x
# y += 1
# print(x)
# print(y)


# x = []
# y = x
# y.append(5)
# print(x)
# print(y)

# s = 'hello world'
# s = s.upper()
# 
# 
# x = 5
# y = 5
# print(id(x))
# print(id(y))
# y += 1
# print(id(x))
# print(id(y))






def reverse(nums):
    # return nums[::-1]
    
    # nums = nums.copy()
    # nums.reverse()
    # return nums
    
    # loop backward and append to the end
    # r = []
    # for i in range(len(nums)-1, -1, -1):
    #     r.append(nums[i])
    # return r
    
    # loop forward and insert at the front
    # r = []
    # for i in range(len(nums)):
    #     print(r)
    #     r.insert(0, nums[i])
    # return r
    
    
    
    nums = nums.copy()
    for i in range(len(nums)//2):
        j = len(nums)-1-i
        
        # t = nums[i]
        # nums[i] = nums[j]
        # nums[j] = t
        
        nums[i], nums[j] = nums[j], nums[i]
        
    
    return nums
        
    


# import math
# def sqrt(x):
#     x = math.sqrt(x)
#     return -x, x
# 
# a, b = sqrt(4)
# 
# print(a)
# print(b)

    
    
    
# nums = ['apples', 'bananas', 'pears', 'cherries']
# print(reverse(nums))



def extract_less_than_ten(nums):
    mylist = []
    for i in range(len(nums)):
        if nums[i] < 10:
            mylist.append(nums[i])
    return mylist

# print(extract_less_than_ten([2, 3, 5, 11, 12]))


def common_elements(nums1, nums2):
    irrons_list = []
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            print(f'{nums1[i]} == {nums2[j]}\t{nums1[i] == nums2[j]}')
            if nums1[i] == nums2[j]:
                irrons_list.append(nums1[i])
    return irrons_list


# print(common_elements(['apples', 'bananas', 'pears'], ['bananas', 'peaches', 'avocados', 'apples']))


#            0          1         2         3           4         5
#         0        1          2        3           4           5         6
# fruits = ['apples', 'bananas', 'pears', 'cherries', 'peaches', 'avocados']
# print(fruits[1:4])


# assign 
# p = print
# p('hello world!')


# s = 'hello world'.split()
# print(s)

def perform_operations(nums, function):
    r = []
    for num in nums:
        r.append(function(num))
    return r

# def square(x):
#     return x*x
# print(perform_operations([1, 2, 3, 4], square))
# print(perform_operations([1, 2, 3, 4], lambda x: x*x))
# min = lambda a, b: a if a < b else b





# a = int(input('enter a number: '))
# b = int(input('enter a number: '))
# op = input('enter an operator: ')
# 
# operators = {
#     '+': lambda a, b: a + b,
#     '-': lambda a, b: a - b
# }
# print(operators[op](a, b))
# 
# 
# 
# if op == '+':
#     print(a + b)
# elif op == '-':
#     print(a - b)




# functions = [print, abs, range, str, float, int]
# for function in functions:
#     print(function, end='\t')
#     print(function(5))
#     print()
# exit()

def combine(nums1, nums2):
    # if len(nums1) != len(nums2):
    #     return None
    min_length = min(len(nums1), len(nums2))
    nums1 = nums1[:min_length]
    nums2 = nums2[:min_length]
    matts_list = []
    for i in range(len(nums1)):
        # matts_list.extend([nums1[i], nums2[i]])
        matts_list.append(nums1[i])
        matts_list.append(nums2[i])
    return matts_list

def matts_idea(matts1, matts2):
    matts_list = matts1.copy()
    for i in range(len(matts2)):
        print(f'{i} {1+i*2}')
        matts_list.insert(1+i*2, matts2[i])
    return matts_list
        
    

# import string
# letters = list(string.ascii_lowercase)
# numbers = list(range(1, len(string.ascii_lowercase)+1))
# 
# letters = letters[:len(letters)//2]
# numbers = numbers[:len(numbers)//2]
# 
# # print(letters)
# # print(numbers)
# 
# # print(combine(['a','b','c'],[1,2,3])) # ['a', 1, 'b', 2, 'c', 3]
# 
# print(matts_idea(letters, numbers))



def find_pair(nums, target):
    # matts_list = []
    # for i in range(len(nums)-1):
    #     if nums[i] + nums[i+1] == target:
    #         matts_list.extend([nums[i], nums[i+1]])
    #         return matts_list
    # return None
    
    
    # if nums[0] + nums[1] == target:
    #     return [nums[0], nums[1]]
    # elif nums[0] + nums[2] == target:
    #     return [nums[0], nums[2]]
    # elif nums[0] + nums[3] == target:
    #     return [nums[0], nums[3]]
    # elif nums[1] + nums[2] == target:
    #     return [nums[1], nums[2]]
    
    pairs = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            # print(f'{nums[i]} {nums[j]}')
            if nums[i] + nums[j] == target:
                pairs.append([nums[i], nums[j]])
    return pairs
    
    
def find_pair_nicole(nums, target):
    pair_list = []
    for i in range(len(nums)):
        x = target - nums[i]
        for j in range(i+1, len(nums)):
            if x == nums[j]:
                pair_list.append(nums[j])
                pair_list.append(nums[i])
    return pair_list

#       0  1  2  3  4
# nums = [5, 6, 2, 3, 1]
# target = 7
# print(find_pair_nicole(nums, target)) # [5, 2]


def merge(nums1, nums2):
    # marinas_list = list(zip(nums1, nums2))
    # marinas_list = [list(l) for l in marinas_list]
    # return marinas_list
    
    marinas_list = []
    for i in range(len(nums1)):
        marinas_list.append([nums1[i], nums2[i]])
    return marinas_list
    
# print(merge([5,2,1], [6,8,2])) # [[5,6],[2,8],[1,2]]


def combine_all(list_of_lists_of_nums):
    shadows_list = []
    for i in range(len(list_of_lists_of_nums)):
        # shadows_list.extend(list_of_lists_of_nums[i])
        for j in range(len(list_of_lists_of_nums[i])):
            shadows_list.append(list_of_lists_of_nums[i][j])
    return shadows_list

# nums = [[5,2,3],[4,5,1],[7,6,3]]
# print(combine_all(nums)) # [5,2,3,4,5,1,7,6,3]


# n! = n*(n-1)!, 1! = 1
# 5! = 5*4*3*2*1
def factorial(n):
    r = 1
    while n > 0:
        # print(f'{r} *= {n}')
        r *= n
        n -= 1
    return r

def factorial_recursive(n):
    
    if n == 1:
        print('returning 1')
        return 1
    print(f'calling {n}*factorial({n-1})')
    r = n*factorial_recursive(n-1)
    print(f'returning {r}')
    return r

# print(factorial_recursive(5))


def fibonacci(n):
    judis_list = [1, 1]
    for i in range(1, n):
        judis_list.append(judis_list[i] + judis_list[i-1])
    return judis_list
        



# print(fibonacci(20))

import sys

def minimum(nums):
    # nums = sorted(nums)
    # return nums[0]
    
    # return min(nums)
    
    if not nums:
        return None
    
    mini = nums[0]
    for num in nums:
        if num < mini:
            mini = num
    return mini
    
    



def maxmimum(nums):
    if not nums: # if nums is a blank list or None
        return None
    
    mini = nums[0]
    for num in nums:
        if num > mini:
            mini = num
    return mini

def mean(nums):
    return sum(nums)/len(nums)
    
    total = 0
    count = 0
    for num in nums:
        total += num
        count += 1
    return total / count

def median(nums):
    nums = sorted(nums)
    if len(nums) % 2 == 0:
        i = len(nums) // 2
        return (nums[i] + nums[i-1]) / 2
    return nums[len(nums)//2]

def mode(nums): # (OPTIONAL)
    current_mode = 0
    mode_count = 0 #number of appearances of current mode
    for i in range(len(nums)):
        count = 0
        for num in nums:
            if num == nums[i]:
                count += 1
            if count > mode_count:
                current_mode = nums[i]
                mode_count = count
    return current_mode

def mode2(nums):
    mode_dict = {}
    for num in nums:
        if num not in mode_dict:
            mode_dict[num] = 1
        else:
            mode_dict[num] += 1
        # print(num, mode_dict)
    
    print(mode_dict)
    mode_tuples = list(mode_dict.items())
    mode_tuples.sort(key=lambda x: x[1], reverse=True)
    print(mode_tuples)
    values = [t[0] for t in mode_tuples if t[1] == mode_tuples[0][1]]
    print(values)


def mode3(nums):
    counts = [0] * (max(nums)+1)
    for num in nums:
        counts[num] += 1
    # print([i for i in range(len(counts))])
    # print(counts)
    max_count = max(counts)
    return [i for i in range(len(counts)) if counts[i] == max_count]
    
    

# def add(a, b):
#     return a + b
# add = lambda a, b: a + b

# import random
# nums = [0,0,0,1,1,3,3,3,4,4,5,5,6,6,6]
# print(nums)
# print(f'min:  {minimum(nums)}')
# print(f'max:  {maxmimum(nums)}')
# print(f'mean: {mean(nums)}')
# print(f'median: {median(nums)}')
# print(f'mode: {mode3(nums)}')


def find_unique(nums):
    kyles_list = []
    for num in nums:
        if num not in kyles_list:
            kyles_list.append(num)
    return kyles_list
    
    # return list(set(nums))
    
nums = [12, 24, 24, 35, 88, 88, 120, 120, 155, 155]
print(list(sorted(nums)))
print(find_unique(nums)) # [12, 24, 35, 88, 120, 155]
