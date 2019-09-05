# filename: random.py
# review: random module & random.choice()
​
# Import Modules
# modules/libraries must be imported for its functions to work
# never name your files the same as module
import random
​
# Define Variables
# [] is an empty list
student_list = []
​
student_list = ["Cameron", "Kendra", "Phillip", "Mattthew", "Nicole", "Sean", "Marina", "Brandon",
"Julian", "Irron"]
​
# Code
​
# len() = to check length
student_list_len = len(student_list)
print(student_list_len)
​
# index() = to find an item by value/name
print("Sean's index:")
print(student_list.index("Sean"))
​
# list[index] = to find an item by index #
# index of 0 = first person
print("First person in list: ")
print(student_list[0])
​
# index of -1 = last person
print("Last person AKA First person starting from the end of list:")
print(student_list[-1])
​
class_in_session = "yes"
​
# random.choice(list)
while class_in_session == "yes":
    random_student = random.choice(student_list)
    print("Random student:")
    print(random_student)
    student_list.remove(random_student)
​
    class_in_session = input("Do you want to choose another student?")
