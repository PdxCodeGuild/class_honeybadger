#filename: random.py
#learning objective: random.choice()

#import modules
#modules or libraries must be imported for its functions to work
#never name your files the same as modules, or the program will attempt to include the file before the library
import random

#define variables
#[] is an empty list
student_list=["Kris","Jen,","Madyson","Judi","JMike","Kurt"]


# Code

#len()=to check length
print(len(student_list))

#index()= to find an item by value/name
print(student_list.index("Kris"))

#list index to find an item by index
print(student_list[0])

#random.choice(list)
print("random student:")
print(random.choice(student_list))
