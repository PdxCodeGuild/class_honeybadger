

import random

import time


def get_time():
    return int(round(time.time() * 1000))





def random_list(n):
    lis = []
    for i in range(n):
        lis.append(random.randint(0,100))
    return lis


def shuffle(lis):
    for i in range(len(lis)):
        j = random.randint(0, len(lis)-1)
        x = lis[j]
        lis[j] = lis[i]
        lis[i] = x
    
        
        


def is_sorted(nums):
    for i in range(len(nums)-1):
        if nums[i] >= nums[i+1]:
            return False
    return True


def bogosort(nums):
    count = 0
    start_time = get_time()
    
    while not is_sorted(nums):
        # print(nums)
        shuffle(nums)
        count +=1
        # print(count)
        
        if count % 1000 == 0:
            print('☠️'*20)
            end_time = get_time()
            time_elapsed = end_time - start_time
            print(f'Number of steps: {count}')
            print(f'Time elapsed: {time_elapsed} milliseconds')
            print(f'Time per step: {time_elapsed/count} milliseconds')
        
    
    
    
    
    
nums = random_list(8)
print(nums)
bogosort(nums)
print(nums)
# shuffle(nums)
# print(nums)
# print(is_sorted([0,4,436457,65,4,634,6]))
# print(is_sorted([0,1,2,3,4,5,6,7]))