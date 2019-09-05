#filename: problem_set3.py

import random

"""#problem 1
def randelem():
    ulist = [1,2,3,4,5]
    return ulist[random.randint(0,4)]
#print(randelem())

#problem 2
def listmkr():
    lis = []
    ad = ''
    while ad != 'done':
        ad = input('num pls...')
        lis.append(ad)
    lis.remove('done')
    return lis
#print(listmkr())"""

"""#problem 3
def evtru():
    lis = []
    elis = []
    for i in range(8):
        lis.append(random.randint(0,10))
    print(lis)
    for i in range(len(lis)):
        if lis[i]%2==0:
            elis.append(lis[i])
    print(elis)
    if len(elis)%2==1:
        return False
    else:
        return True            
#print(evtru())"""

#problem 4
"""def bkbt():
    blis = []
    flis = []
    wlis = []
    a = 0
    for i in range(8):
        blis.append(random.randint(0,99))
    print(blis)
    for i in range(len(blis)):
        if i%2!=0:
            flis.append(blis[i])
    print(flis)
    while a <= len(blis):
       if index %2==0:
            wlis.append(blis[index])
            a += 2
        else:
            break        
    print(wlis)
#print(bkbt())"""

#problem 5

"""#problem 6
def movelownums():
    lis = []
    elis = []
    for i in range(8):
        lis.append(random.randint(0,20))
    for i in range(len(lis)):
        if lis[i]<10:
            elis.append(lis[i])
    return elis
print(movelownums())"""

"""def movelownums2()
    num = [random.randint(0,20) for i in range(10)]
    elis = [num for num in num if num<10]
    print(num)
    return elis
print(movelownums())"""

#problem 7
"""def comel():
    lis = [random.randint(0,10) for i in range(10)]
    elis = [random.randint(0,10) for i in range(len(lis))]
    flis = []
    for i in range(len(lis)):
        if lis[i] == elis[i]:
            flis.append(lis[i])
    print(lis)
    print(elis)
    return int(len(flis))
print(comel())"""


