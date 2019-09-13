#filename: lab14_picksixx.py

import random

def sixgen():
    ulist = []
    for i in range(6):
        ulist.append(random.randint(0,99))
    return ulist

winlist = sixgen()

def matcher(plylist,winlist):
    matchnum = 0
    for i in range(6):
        if plylist[i] == winlist[i]:
            matchnum = matchnum + 1
    return matchnum

def przcalc():
    prizelist = [0,4,7,100,50000,1000000,25000000]
    prize = prizelist[matcher(plylist,winlist)]
    return prize

bal = 0
investment = 0
earnings = 0

for i in range(100000):
    plylist = sixgen()
    if przcalc() > 0:
        print(plylist,winlist,przcalc())
    bal = bal - 2
    bal = bal + przcalc()
    investment += 2
    earnings += przcalc()

roi = (earnings-investment)/investment

print(f'final balance is {bal}\nyou earned {earnings}\nand spent {investment}')
print(f'your ROI equals {roi}')







