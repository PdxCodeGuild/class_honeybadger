#filename: lab10_avg_numbers.py

nums = []

numtotal = 0

myflag = True
while myflag == True:
    usrin = input(f'Enter a number or done\n')
    if usrin == 'done':
        myflag = False
    else:
        usrin = float(usrin)
        nums.append(usrin)

nums.sort()
print(nums)

for i in range(len(nums)):
    
    numtotal = numtotal + nums[i]
    avg = numtotal / len(nums)

median = nums[int(len(nums)/2)]

def mode(nums):
    current_mode = 0
    scount = 0
    for i in range(len(nums)):
        count = 0
        for num in nums:
            if num == nums[i]:
                count += 1
        if count > scount:
            scount = count
            current_mode = nums[i] 
                
    return current_mode

mode = mode(nums)

print('mode is ',mode)

print('median is ',median)

print('total is ',numtotal)

print('average is',avg)



