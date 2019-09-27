# filename: problem_set1.py

def oden(a): # Write a function that tells whether a number is even or odd (hint, compare a/2 and a//2, or use a%2)
    if a%2 == 1:
        return str('odd')
    else:
        return str('even')
# a=int(input("number pls"))
# print(oden(a))

def pone(b,c): #Write a function that takes two ints, a and b, and returns True if one is positive and the other is negative.
    if b < 0 and c > 0:
        return True
    elif b > 0 and c < 0:
        return True
    else:
        return False
# b=int(input('enter num'))
# c=int(input('enter num2'))
# print(pone(b,c))

def otoh(d): # Write a function that returns True if a number within 10 of 100.
    
    if 90<d<110:
        return True
    else:
        return False

# d=int(input('num pls'))
# print(otoh(d))

def maxt(e,f,g): # Write a function that returns the maximum of 3 parameters.
    
    e=int(input('gimme'))
    f=int(input('gimme2'))
    g=int(input('gimme3'))
    
    if e>f and e>g:
        return e
    elif f>e and f>g:
        return f
    elif g>e and g>f:
        return g
    else:
        return str('ow')
# e=int(input('gimme'))
# f=int(input('gimme2'))
# g=int(input('gimme3'))
# print(maxt(e, f, g))

def powers(): # Print out the powers of 2 from 2^0 to 2^20
    return str.strip(str([2**i for i in range(20)]), '[]')
# print(powers())