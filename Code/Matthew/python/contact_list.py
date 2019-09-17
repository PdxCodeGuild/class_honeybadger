
# absolute path
# with open(r'C:\Users\flux\programs\class_honeybadger\1 Python\data\contacts.csv', 'r') as file:
with open('../../../1 Python/data/contacts.csv', 'r') as file:
    text = file.read()


# print([{[line.split(',') for line in text.split('\n')][0][i]:[line.split(',') for line in text.split('\n')][1:][j][i] for i in range(len([line.split(',') for line in text.split('\n')][0]))} for j in range(len([line.split(',') for line in text.split('\n')][1:]))])




contacts = []
text = text.split("\n")
# print(text)
for i in range(len(text)):
    contacts.append(text[i].split(","))
contacts_key = contacts.pop(0)
print(contacts_key)
print(contacts)
# contact_list = [{contacts_key[i]:contacts[j][i] for i in range(len(contacts_key))} for j in range(len(contacts))]
contact_list = []
for i in range(len(contacts)):
    contact_dict = {}
    for j in range(len(contacts_key)):
        contact_dict[contacts_key[j]] = contacts[i][j]
    contact_list.append(contact_dict)
print(contact_list)





# contacts = [
#     {'name':'matthew', 'favorite fruit':'blackberries', 'favorite color':'orange'},
#     {'name':'sam', 'favorite fruit':'pineapple' ...}
# ]

# ['name', 'age', 'email', 'favorite color']
# [['joe', '34', 'joe@gmail.com', 'blue'], ['jane', '43', 'jane@gmail.com', 'green'], ['jill', '65', 'jill@gmail.com', 'orange']]