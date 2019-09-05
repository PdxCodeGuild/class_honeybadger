import string

def double_letters(word):
    double = ""
    for char in word:
        double +=char*2
    return double
        
#print(double_letters('taco'))
        
def missing(word):
    text = []
    for i in range(len(word)):
        text.append(word[:i] + word[i+1:])
    return text

# print(missing('kitten'))
#print('hello'[:3]) 
#print('hello'[4:]) 

def latest(word):
    # latest_list = []
    # for char in word:
    #     latest_list.append(char)
    # latest_list = list(word)
    # return sorted(latest_list)[-1]
    return sorted(list(word))[-1]

# using a list comprehension
def latest2(word):
    word = [char for char in word]
    word.sort()
    return word[-1]

# def latest3(word):
# 



print(latest("hjfoiajefaewnmf"))




# print(list(reversed('hello')))
# print(list(range(5, 100)))
# print(list(reversed(sorted(range(0, 100)))))


# fruits = ['apples', 'bananas', 'pears', 'cherries']
# # fruits.sort()
# 
# print(list(reversed('apple')))
# 
# fruits_sorted = sorted(fruits)
# first_fruit = fruits_sorted[0]
# 
# print(fruits)
# print(fruits_sorted)









# words = 'Hello world, it\'s a beautiful beautiful day out isn\'t it?'
# words = words.split(' ')

# # map
# words = [word.replace('\'', '') for word in words]
# words = [word.strip(',?') for word in words]
# words = [word.lower() for word in words]
# # filter
# words = [word for word in words if len(word) < 5]

# words2 = []
# for i in range(len(words)):
#     word = words[i].replace('\'', '').strip(',?').lower()
#     if len(word) < 5:
#         words2.append(word)
# words = words2

# for i in range(len(words)):
#     if len(words[i]) > 5:
#         words.remove(words[i])

# i = 0
# while i < len(words):
#     if len(words[i]) > 5:
#         words.remove(words[i])
#     else:
#         i += 1


print(' '.join(words))









