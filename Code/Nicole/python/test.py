# test.py

def fibonacci(num):
    num_list = list(range(1, num + 1))
    print(num_list)
    my_list = []
    # my_list.append(num_list[i])
    # for i in range(len(num_list)):
    #     print(num_list[i])
    #     print(num_list[i+1])
    #     print(num_list[i+2])
    #     my_list.append(num_list[i-1] + num_list[i-2])
    return my_list

print(fibonacci(8))