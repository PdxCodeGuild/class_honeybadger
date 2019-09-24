# notes_lists.py

# joining a list:
fruits = ["apple", "banana", "orange"]

for x in fruits:
    print("".join(x), end = " ")
print()


# list comprenesion of the above statement
print(*["".join(x) for x in fruits])

