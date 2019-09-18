# filename: lab23_contactlist.py

with open('contacts.csv', 'r') as f:
    text = f.read()
    
print(text)
contacts = [line.split(',') for line in text.split('\n')]
contacts_key = contacts.pop(0)
contact_dic = [{contacts_key[i]:contacts[j][i] for i in range(len(contacts_key))} for j in range(len(contacts))]
# print(contact_dic)


while True:
    
    user_input = input('Press 1 to add new contact \n Press 2 to retrieve a contact \n Press 3 to update a contact \n Press 4 to delete a contact \n Press 5 to view all contacts \n Press 6 to exit \n')
    
    if user_input in ['1','2','3','4','5','6']:
        
        if user_input == '1':
            print('Input new contact info\n')
            new_contact = [input('name: '),input('age: '),input('email: '),input('favorite color: ')]
            new_contact_entry = {contacts_key[i]:new_contact[i] for i in range(len(contacts_key))}
            contact_dic.append(new_contact_entry)
            print(f'{new_contact[0]} added to contacts')

        if user_input == '2':
            found = False
            name_search = input('Input name to retrieve contact info: ')
            for item in contact_dic:
                if name_search in item['name']:
                    print(item)
                    found = True
            if not found:
                print('Not in contact list')
        
        if user_input == '3':
            found = False
            name_search = input('Input name to retrieve contact: ')
            for item in contact_dic:
                if name_search in item['name']:
                    update_value_key = input('What value you like to update? ')
                    if update_value_key in contacts_key:
                        i = contacts_key.index(update_value_key)
                        item[update_value_key] = input('Input new value: ')
                    found = True
            if not found:
                print('Not in contact list')
        
        if user_input == '4':
            found = False
            name_search = input('Input name to retrieve contact: ')
            for item in contact_dic:
                if name_search in item['name']:
                    contact_dic.remove(item)
                    print(f'{name_search} removed from contacts')
                    found = True
            if not found:
                print('Not in contact list')
        
        if user_input == '5':
            print(contact_dic)
        
        if user_input == '6':
            with open('contacts.csv', 'w') as f:
                # f.write(f'{",".join(contacts_key)}\n') 
                lines = [f'{",".join(contacts_key)}']   
                for item in contact_dic:
                    line = []
                    for key, value in item.items():
                        line.append(value)
                    lines.append(f'{",".join(line)}')
                f.write('\n'.join(lines))
            exit()
                    
                
    
    else:
        print('Invalid entry...')
        continue