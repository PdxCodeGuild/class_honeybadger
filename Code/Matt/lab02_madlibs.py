import random


game_in_session = 'yes'
while game_in_session == 'yes':
    user_name = input('What is your name?: ')
    print(f'Hello {user_name} lets get some words from you!')

    adj_list = input('Give me 3 adjectives: ')
    adj_list = adj_list.split()
    rand_adj = random.choice(adj_list)
    rand_adj2 = random.choice(adj_list)


    noun_1 = input('Give me a noun: ')
    verb_1 = input('Give me a past tense verb: ')
    adverb1 = input('Give me an adverb: ')
    # adj_2 = input('Give me another adjective: ' )
    noun_2 = input('Give me another noun: ')




    print("Here is your madlibs!")
    print(f'Today I went to the zoo. I saw a {rand_adj} {noun_1} jumping up and down in its tree.He {verb_1} {adverb1} through the large tunnel that led to its {rand_adj2} {noun_2}.')

    game_in_session = input('Do you want to do another madlib? If your done type "done": ').lower().strip()
