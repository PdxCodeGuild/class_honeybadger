

import random

# O(1)
def add(a, b):
    return a + b

# O(n)
def min(nums):
    running_min = 0
    for num in nums:
        if num < running_min:
            running_min = num
    return running_min

# O(n^2)
def find_duplicates(nums):
    dups = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                dups.append(nums[i])
    return dups
                
# bosort is O(n!)

