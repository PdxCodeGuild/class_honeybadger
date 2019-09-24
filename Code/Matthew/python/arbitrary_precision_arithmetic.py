

# class Person:
#     def __init__(self, full_name):
#         name = full_name.split(' ')
#         self.first_name = name[0]
#         self.last_name = name[1]
# 
#     def reproduce(self, other_person):
#         full_name = self.first_name + '-jr' + ' ' + self.last_name + '-' + other_person.last_name
#         return Person(full_name)
# 
#     def __str__(self):
#         return self.first_name + ' ' + self.last_name
# 
# 
# joe = Person('joe shmoe')
# print(joe)
# jim = Person('jim slim')
# print(jim)
# joe_jr = joe.reproduce(jim)
# jim_jr = jim.reproduce(joe)
# print(jim_jr)



# class Person:
#     def __init__(self, name, gender=None):
#         self.name = name
#         self.email = name.lower().replace(' ', '_') + '@gmail.com'
#         self.gender = gender
#         # self.otherthing = 'hello world!'
# 
#     def say_hello(self):
#         print(self.name + ' says hello!')
# 
# person = Person('Joseph Shmoesef', 'maleish')
# person = Person('Joseph Shmoesef')
# print(person.gender)
# person.say_hello()
# Person.say_hello(person) # dont it this way
# print(person.email)
# 
# exit()




# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
# 
#     def add(self, v):
#         return Vector(self.x + v.x, self.y + v.y)
# 
#     def __add__(self, v):
#         return Vector(self.x + v.x, self.y + v.y)
# 
#     def __sub__(self, v):
#         return Vector(self.x - v.x, self.y - v.y)
# 
#     def __str__(self):
#         return f'({self.x},{self.y})'
# 
#     def __len__(self):
#         return 2
# 
#     def __floordiv__(self, b):
#         print('hello!')
# 
# 
# 
# 
# a = Vector(5, 6)
# print(len(a))
# print(a)
# b = Vector(2, 3)
# print(b)
# # c = a.add(b)
# c = a + b
# # print(v.x, v.y)
# print(c)
# 
# d = a - b
# print(d)
# 
# e = a // b
# print(e)
# 
# c = a.x // 2
# c = a // 2


# x = 10
# for i in range(10):
#     print(x)
#     x **= 2



class BigInt:
    def __init__(self, num_str):
        # if type(num_str) is str:
        num_list = []
        for i in range(len(num_str)):
            num_list.append(int(num_str[i]))
        num_list.reverse()
        self.nums = num_list
    
    def __str__(self):
        # copy_list = self.nums.copy()
        # copy_list.reverse()
        # return "".join([str(copy_list[i]) for i in range(len(copy_list))])
        
        return ''.join([str(v) for v in reversed(self.nums)])
        
    
    def __add__(self, nums_2):
        
        if len(self.nums) != len(nums_2.nums):
            self.nums.append(0)
        
        remainder = 0
        calculation = []
        for i in range(len(self.nums)):
            # v1 = 0
            # v2 = 0
            if i < len(self.nums):
                v1 = self.nums[i]
            else:
                v1 = 0
            
            if i < len(nums_2.nums):
                v2 = nums_2.nums[i]
            else:
                v2 = 0
            
            result = v1 + v2 + remainder
            if result < 10:
                remainder = 0
                calculation.append(result)
            else:
                calculation.append(result % 10)
                remainder = 1
        
        if remainder == 1:
            calculation.append(remainder)
        
        calculation.reverse()
        calculation_str = "".join([str(calculation[i]) for i in range(len(calculation))])
        calculation_str = calculation_str.lstrip('0')
        return BigInt(calculation_str)
                
                
    


# x = BigInt('3246234234243')
# print(x.nums)
# print(x)

# print(type(x.nums))
# y = BigInt('9812342')
# print(y.nums)
# print(y)

x = BigInt('87')
y = BigInt('20')
z = x + y # x is self and y is nums_2

print(z) # 




# a = 5
# b = 6
# print(5*6)
# r = 0
# for i in range(b):
#     r += a
# print(r)





