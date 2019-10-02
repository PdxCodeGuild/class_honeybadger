



with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    print(lines)
    text = file.read()
    print(text)

    contacts = []
    text = text.split("\n")
    print(text)
    
