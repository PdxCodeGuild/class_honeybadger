# lab_optional_sock_sorter_v2.py

import random

def sock_sorter():
    sock_types = ["ankle", "crew", "calf", "thigh"]
    sock_colors = ["pink", "aqua", "gray"]
    socks = []
    socks_sorted = {}
    socks_leftover = []
    
    while len(socks) < 101:
        for a in range(len(sock_types)):
            sock_a = random.choice(sock_types)
            for b in range(len(sock_colors)):
                color_b = random.choice(sock_colors)
            socks.append((sock_a, color_b))
    
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

sock_sorter()