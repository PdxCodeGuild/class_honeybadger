# practice_3_lists_prob9.py

def find_pair(nums, target):
    target = int(target)
    pair_list = []
    for i in range(len(nums)):
        x = target - nums[i]
        for j in range(i+1, len(nums)):
            if x == nums[j]:
                pair_list.append(nums[j])
                pair_list.append(nums[i])
    return pair_list


num_list = [5, 6, 2, 3]
target_num = 7
print(find_pair(num_list, target_num)) # [5, 2]