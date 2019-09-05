
def add(a, b):
    return a + b

# print(add(5, 2))
# print(add(6, 7))



def is_even(num):
    if num%2 == 0:
        return True
    return False
    #if num%2 == 0:   #alt2
#print(is_even(5))
    

def opposite(x,y):
    return (x <0 and y>0) or (x>0 and y<0)
        #return True
    #return False
        
#print(opposite(5,3))


def near_100(num):
    return num in range(90,111)
        #return True
    #return False
#print(near_100(110))

def max_of_three(x,y,z):
    if x >y and x >z:
        return x
    elif y >z and y>x:
        return y
    return z 
#print(max_of_three(13,-8,11))
        
        
def power2():
    for num in range(0,21):
        print(2**num)
    
    
#power2()
print([2**num for num in range(0,21)])

    


