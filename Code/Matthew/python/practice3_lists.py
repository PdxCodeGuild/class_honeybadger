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


print(common_elements(['apples', 'bananas', 'pears'], ['bananas', 'peaches', 'avocados', 'apples']))

    
