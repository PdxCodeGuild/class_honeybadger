
def rot13(user_input):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    output = ""

    for char in user_input:
        output += alphabet[(alphabet.find(char)+13)%26]
    return output

user_input = input("Enter a message")

print(rot13(user_input))

    
