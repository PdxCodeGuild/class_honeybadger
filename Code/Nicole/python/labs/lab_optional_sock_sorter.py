# lab_optional_sock_sorter.py

# Generate a list of 100 random socks, randomly chosen from a set of types
# Find the number of duplicates and loners for each sock type. 
# -- Hint: dictionaries are helpful here.

import random

def sock_sorter():
    sock_types = ['ankle', 'crew', 'calf', 'thigh']
    socks = []
    socks_sorted = {}
    socks_leftover = []
    
    while len(socks) < 101:
        for i in range(len(sock_types)):
            socks.append(random.choice(sock_types))
    
    for x in range(len(socks)):
        if socks[x] not in socks_sorted:
            socks_sorted[socks[x]] = 1
        else:
            socks_sorted[socks[x]] += 1
    
    for key in socks_sorted:
        if socks_sorted[key] % 2 == 1:
            socks_leftover.append(key)
        
    print("Here are the socks in your laundry you sorted:")
    
    for a, b in socks_sorted.items():
        print(a, b)
    
    if len(socks_leftover) > 1:
        print("And you also have the following socks without a pair:")
    elif len(socks_leftover) == 0:
        print("You found them all!")
    else:
        print("And you also have the following sock without a pair:")
    
    for c in range(len(socks_leftover)):
        print(socks_leftover[c])

['crew', 'thigh']
socks = [('black', 'crew'), ('magenta', 'thigh')]
socks[0][1]

socks = [{'color': 'black', 'type': 'crew'},]
socks[0]['color']
    
sock_sorter()