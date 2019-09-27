#filename: problem_set5.py

# problem 1
#Write a comprehension to generate the first 10 powers of two.
def p1():
    return [2**x for x in range(10)]
# print(p1())

# problem 2
# Write a comprehension to generate the first 10 even numbers.
def p2():
    return [x for x in range(21) if x%2==0 and x>0]
# print(p2())

# problem 3
# Write a dictionary comprehension to swap keys and values of a given dictionary. So {'a': 1, 'b': 2} would become {1: 'a', 2: 'b'}.
def p3():
    dict = {'a':1, 'b':2, 'c':3, 'd':4}
    return {v:k for k, v in dict.items()}
# print(p3())

# problem 4
# Write a dictionary comprehension to print each letter of the alphabet and its correstponding ASCII code (check out ord)
import string
alp = string.ascii_lowercase
def p4(alp):
    return {alp[i]:ord(alp[i]) for i in range(len(alp))}
# print(p4(alp))
