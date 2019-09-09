# test.py

def combine(nums1, nums2):
    my_list = []
    for i in range(len(nums1)):
        my_list.append(nums1[i])
        my_list.append(nums2[i])
    return my_list
    
l1 = ["a", "b", "c"]
l2 = [1, 2, 3]

print(combine(l1, l2))