#filename: problem_set1.py

def oden(a):
    if a%2 == 1:
        return str('odd')
    else:
        return str('even')
#a=int(input("number pls"))
#print(oden(a))

def pone(b,c):
    if b < 0 and c > 0:
        return True
    elif b > 0 and c < 0:
        return True
    else:
        return False
#b=int(input('enter num'))
#c=int(input('enter num2'))
#print(pone(b,c))

def otoh(d):
    if 90<d<110:
        return True
    else:
        return False
#d=int(input('num pls'))
#print(otoh(d))

def maxt(e,f,g):
    if e>f and e>g:
        return e
    elif f>e and f>g:
        return f
    elif g>e and g>f:
        return g
    else:
        return str('ow')
#e=int(input('gimme'))
#f=int(input('gimme2'))
#g=int(input('gimme3'))
#print(maxt(e,f,g))

for i in range(21):
    print(2**i)
