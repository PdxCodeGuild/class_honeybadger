# practice_3_lists_prob6.py

# define function

def extract_less_than_10(a):
    new_list = []
    for x in a:
        if x <= 9:
            new_list.append(x)
    return(new_list)
    

number_list = list(range(0,20))

print(extract_less_than_10(number_list))

# list comprehension

comp_list = [x for x in range(0, 20) if x <= 9]
print(comp_list)