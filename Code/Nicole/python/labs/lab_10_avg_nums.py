# avg_nums.py

#Start with the following list, iterate through it, keeping a 'running sum', then divide that sum by the number of elements in that list. Remember len will give you the length of a list.

# define number list

nums = [5, 0, 8, 3, 4, 1, 6]

running_sum = 0

for num in range(len(nums)):
    running_sum += nums[num]

avg_sum = running_sum / len(nums)
print(avg_sum)
