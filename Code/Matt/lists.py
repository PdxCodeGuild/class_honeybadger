list = [1,16,2,3,7,4,3,7,8,45,56]


def extract_less_than_ten(a_list):
    new_list = []
    for i in range(len(a_list)):
        if list[i] < 10:
            new_list.append(a_list[i])
    return new_list

print(extract_less_than_ten(list))
