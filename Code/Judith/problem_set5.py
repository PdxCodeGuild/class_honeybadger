#filename: problem_set5.py

#problem 1
def p1():
    return [2**x for x in range(10)]
#print(p1())

#problem 2
def p2():
    return [x for x in range(21) if x%2==0 and x>0]
#print(p2())

#problem 3
def p3():
    dict = {'a':1, 'b':2, 'c':3, 'd':4}
    return {v:k for k, v in dict.items()}
#print(p3())

#problem 4
import string
alp = string.ascii_lowercase
def p4(alp):
    return {alp[i]:ord(alp[i]) for i in range(len(alp))}
#print(p4(alp))
