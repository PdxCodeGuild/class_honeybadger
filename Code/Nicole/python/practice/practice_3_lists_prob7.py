# practice_3_lists_prob7.py

# define function

def common_elements(a,b):
    new_list = []
    for x in a:
        for y in b:
            if x == y:
                new_list.append(x)
    return new_list
    
list_1 = [1, 2, 3, 4, 5]
list_2 = [3, 4, 5, 6, 7]
# should return [3, 4, 5]

list_3 = [1, 2, 3, 4, 5]
list_4 = [1+1, 2+1, 4+1, 5+1, 6+1]
# should return [2, 3, 5]

print(common_elements(list_1, list_2))
print(common_elements(list_3, list_4))