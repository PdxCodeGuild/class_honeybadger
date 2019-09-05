#filename: avg_numbers.py

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

print(nums)

for i in range(len(nums)):
    
    numtotal = numtotal + nums[i]
    avg = numtotal / len(nums)

print(numtotal)

print(avg)



