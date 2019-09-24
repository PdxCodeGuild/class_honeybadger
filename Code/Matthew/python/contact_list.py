


# fruits = {'apples': 1, 'bananas': 2, 'pears': 3}
# del fruits['pears']
# print(fruits)
# exit()


# absolute path
# with open(r'C:\Users\flux\programs\class_honeybadger\1 Python\data\contacts.csv', 'r') as file:

def load_contacts(path):
    with open(path, 'r') as file:
        text = file.read()

    # print([{[line.split(',') for line in text.split('\n')][0][i]:[line.split(',') for line in text.split('\n')][1:][j][i] for i in range(len([line.split(',') for line in text.split('\n')][0]))} for j in range(len([line.split(',') for line in text.split('\n')][1:]))])

    contacts = []
    text = text.split("\n")
    # print(text)
    for i in range(len(text)):
        if text[i] == '':
            continue
        contacts.append(text[i].split(","))
    contacts_key = contacts.pop(0)
    # contact_list = [{contacts_key[i]:contacts[j][i] for i in range(len(contacts_key))} for j in range(len(contacts))]
    contact_list = []
    for i in range(len(contacts)):
        contact_dict = {}
        for j in range(len(contacts_key)):
            contact_dict[contacts_key[j]] = contacts[i][j]
        contact_list.append(contact_dict)
    return contact_list



def save_contacts(path, contacts):
    with open(path, 'w') as file:
        file.write(contacts_to_string(contacts))


# name,age,email,favorite color
# joe,34,joe@gmail.com,blue
# jane,43,jane@gmail.com,green
# jill,65,jill@gmail.com,orange

def pretty_print(contact):
    return ','.join(contact.values())

def contacts_to_string(contacts):
    output = ''
    output += ','.join(contacts[0].keys()) + '\n'
    for i in range(len(contacts)):
        output +=  pretty_print(contacts[i]) + '\n'
    return output
    
def find_contact_with_name(name, contacts):
    for i in range(len(contacts)):
        if contacts[i]['name'] == name:
            return contacts[i]
    return None
    

def create(contacts):
    headers = list(contacts[0])
    created = {}
    for i in range(len(headers)):
        user_prompt = input(f'Please enter your {headers[i]}: ')
        created[headers[i]] = user_prompt
    contacts.append(created)
    print(pretty_print(created))

def retrieve(contacts):
    user_prompt = input('Please enter a name: ')
    contact = find_contact_with_name(user_prompt, contacts)
    if contact:
        print(pretty_print(contacts[i]))
    else:
        print('Contact not found')

def update(contacts):
    headers = list(contacts[0])
    contact_name = input('Please enter the name of the contact you would like to update please: ')
    contact_attribute = input('Which attribute would you like to change? ')
    contact_update_value = input('What is the attribute\'s new value? ')
    contact = find_contact_with_name(contact_name, contacts)
    if contact:
        contact[contact_attribute] = contact_update_value
    else:
        print('Contact not found')
    


def delete(contacts):
    user_prompt = input('Please enter the name of the contact that you would like to delete please: ')
    # for i in range(len(contacts)):
    #     if contacts[i]['name'] == user_prompt:
    #         del contacts[i]
    contact = find_contact_with_name(user_prompt, contacts)
    if contact:
        yesno = input('Are you sure? ')
        if yesno == 'yes':
            contacts.remove(contact)
    else:
        print('Contact not found')
    

def cruddy_repl(path):
    contacts = load_contacts(path)
    user_input = ''
    while user_input != 'done':
        print(contacts_to_string(contacts).replace(',','\t\t'))
        user_input = input('Hey you, whatcha wanna do? Please type \'create\', \'retrieve\', \'update\', \'delete\', or \'done\' when finished:\n')
        user_input = user_input.lower()
        
        if user_input == 'create':
            create(contacts)
        elif user_input == 'retrieve':
            retrieve(contacts)
        elif user_input == 'update':
            update(contacts)
        elif user_input == 'delete':
            delete(contacts)
        elif user_input == 'done':
            print('Thank you, come again! =D')
            break
        else:
            # print('What are you thinking‽‽')
            print('What are you thinking!?')
            break
        # print(contacts)
    
        
    save_contacts(path, contacts)

path = '../../../1 Python/data/contacts.csv' # input('Where\'s your data? ')
cruddy_repl(path)







