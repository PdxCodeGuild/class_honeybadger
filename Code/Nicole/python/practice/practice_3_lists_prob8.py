# practice_3_lists_prob8.py

# still not finished with this exercise ...

# define function

def combine(a, b):
    new_list = []
    index = 0
    for x in a[index]:
        new_list.append(x)
        for x in b:
            new_list.append(x)
        index +=1
    return new_list

list_1 = [1, 2, 3, 4, 5]
list_2 = ["a", "b", "c", "d", "e"]

print(combine(list_1, list_2))