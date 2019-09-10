




# def catdog_count():
#
#     string = "catdog"
#     dog_count = 0
#     cat_count = 0
#
#     while 'cat' in string:
#         cat_count +=1
#         string = string.replace('cat', 1)
#         print(cat_count)
#     while 'dog' in string:
#         dog_count +1
#         string = string.replace('dog', 1)
#         print(dog_count)
#     if dog_count == cat_count:
#         print("True")
#     else:
#         print("False")
#
# catdog_count()


string = "catdogdog"
dog_count = 0
cat_count = 0
cat_count = string.count("cat")
dog_count = string.count("dog")

if cat_count == dog_count:
    print("True")
else:
    print("false")
