# notes.py

# add end = ' ' to specify the end and not default to a new line (\n)
print("\nAdd 'end' to change the default end of a print statement:")

for x in range(10):
    print(x, end=" ")
print()

# joining a list:
print("\nThis joins a list:")

fruits = ["apple", "banana", "orange"]

for x in fruits:
    print("".join(x), end = " ")
print()
# list comprenesion of the above statement
print(*["".join(x) for x in fruits])