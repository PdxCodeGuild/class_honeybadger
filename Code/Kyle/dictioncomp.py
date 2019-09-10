

import string

# for char in string.ascii_lowercase:
#     print({char: ord(char)})

def ascii_value():
    return {char: ord(char) for char in string.ascii_lowercase}

print(ascii_value())
