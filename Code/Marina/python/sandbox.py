import string

# def double_letters(word):
#     double = ''
#     for char in word:
#         double +=char*2
#     return double
#
# # print(double_letters('cat'))
#
# def missing(word):
#     text = []
#     for i in range(len(word)):
#         text.append(word[:i] + word[i+1:])
#     return text

# print(missing('tango'))
# print('marina'[:3])
# print('ciaoooo'[4:])

# def latest(word):
#     latest_list = []
#     for char in word:
#         latest_list.append(char)
#     latest_list = list(word)
#     return sorted(latest_list)[-1]
    # return sorted(list(word))[-1]

# def latest2(word):
    # word = [char for char in word]
    # word.sort()
    # return word[-1]

# def latest3(word):
#     word = [char for char in word]
#     print (word)
#     word = [ord(char) for char in word]
#     print (word)
#     highest_letter_code = max(word)
#     print (highest_letter_code)
#     return chr(highest_letter_code)
#
# print(latest3('absolutely'))

# print(list(reversed('hello')))
# print(list(range(5, 10)))
# print(list(reversed(sorted(range(0, 10)))))

# fruits = ['apples', 'berries', 'watermelon', 'apricots', 'bananas']
# fruits.sort()
#
# print(list(reversed(fruits)))
#
# fruits_sorted = sorted(fruits)
# first_fruit = fruits_sorted[0]
#
# print(fruits)
# print(fruits_sorted)

# words = 'I understand that that\'s a bad example,?'
# words = words.split(' ')
# # print(words)
# # words = [word.replace('\'', '') for word in words]
# words = [word.strip(',?') for word in words]
# # print(words)
# words = [word.lower() for word in words]
#
# words = [word for word in words if len(word) < 5]
#
# words2 = []
# for i in range(len(words)):
#     word = words[i].replace('\'', '').strip(',?').lower()
#     if len(word) < 5:
#         words2.append(word)
# words = words2
#
#
# for i in range(len(words)):
#     if len(words[i]) > 5:
#         words.remove(words[i])
# print(words)
#
# i = 0
# while i < len(words):
#     if len(words[i]) > 5:
#         words.remove(words[i])
#     else:
#         i +=1
# print(' '.join(words))

def count_occurances(text, word):
    count = 0
    for i in range(len(text)-(len(word)-1)):
        print(text)
        print(' '*i + word)
        for j in range(len(word)):
            if text[i+j] != word[j]:
                break
        else:
            count +=1

    matches = True
    for j in range(len(word)):
        if text[i+j] != word[j]:
            matches = False
            break
        if matches:
            count += 1
        if text[i:i+len(word)] == word:
            count += 1

    return count
#     print(count)
# print(count_occurances('i love love', 'love'))

def count_hi(text):
    count = 0
    word = 'hi'
    for i in range(len(text)-1):
        if text[i+0] == word[0] and text[i+1] == word[1]:
            count += 1
    return count

def count_cat(text):
    count = 0
    word = 'cat'
    for i in range(len(text)-2):
        if text[i+0] == word[0] and text[i+1] ==word[1] and text[i+2] ==word[2]:
            count ++ 1
    return count

def count_home(text):
    count = 0
    for i in range(len(text)-3):
        if text[i+0] == 'h' and text[i+1] == 'o' and text[i+2] == 'm' and text[i+3] == 'e':
            count += 1
    return count

    print(count_hi('hihih'))
print(count_hi('hihi')) # 2
print(count_hi('sdfsjfdlskdfhi')) # 1
print(count_hi('hello hi how are you hihihi')) # 4

print(count_occurances('hello cat 123 cat', 'cat'))
