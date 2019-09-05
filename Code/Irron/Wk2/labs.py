'''
Lab 19: Palindrome and Anagram

A palindrome is a word that's the same forwards or backwards, e.g. racecar. 
Another way to think of it is as a word that's equal to its own reverse.

Write a function check_palindrome which takes a string, and returns True if the string's a 
palindrome, or False if it's not

>>> enter a word: racecar
>>> 'racecar' is a palindrome

>>> enter a word: palindrome
>>> 'palindrome' is not a palindrome

'''
# def check_palindrome(word):
#     word = word
#     word_reverse = word[::-1] #start =0, stop=0, step =-1, meaning start at end and reverse word
#     if word == word_reverse:
#         print('True')
#     else:
#         print('False')
    
#     return word

# word = 'racecar'   
# print(check_palindrome(word))

'''
Lab 19 Palidrome and Anagram
Two words are anagrams of each other if the letters of one can be rearranged to fit the other. 
e.g. anagram and nag a ram.

Write another function check_anagram that takes two strings as parameters and returns 
True if they're anagrams of each other, False if they're not. The procedure for comparing 
the two strings is as follow:

    1. Convert each word to lower case (lower)
    2. Remove all the spaces from each word (replace)
    3. Sort the letters of each word (sorted)
    4. Check if the two are equal

>>> enter the first word: anagram
>>> enter the second word: nag a ram
>>> 'anagram' and 'nag a ram' are anagrams

'''
# def check_anagram(word1, word2):
#     word1 = word1.lower().replace(' ','') #sort is method only to be used on list. does not have attribute
#     word2 = word2.lower().replace(' ','')
#     word1_list = list(word1) #converting string to a list
#     word1_list.sort() #sorting a list. sort method sorts in place, no need to create a variable. 
#     print(word1_list)

#     # if word1==word2:
#     #     print('The words are equal')
#     #     print('The words are not equal')

#     return word1,word2


# print(check_anagram('GOOD MORNING','HAVE a woNDERFUL DAy'))


'''
Lab 13: Rot13
Write a program that prompts the user for a string, and encodes it with ROT13. For each character, find the corresponding 
character, add it to an output string. Notice that there are 26 letters in the English language, so encryption is the 
same as decryption.

'''
# ######CIPHER#################
#Lab 13: Rot13
# import string
# alphabet = string.ascii_lowercase*2

# def cipher():
#     mod_phrase = '' #our solution will be added here
#     for x in user_input:
#         if x == ' ':  #used for multiple words with space..doesnt work
#             mod_phrase += x #adding letter to mod_phrase
#         mod_phrase += alphabet[alphabet.find(x) + deg%26] #finding index value of x within string alphabet 
#     return mod_phrase

# deg = int(input(('give a degree of rotation')))
# user_input = input('enter a string')

# print(cipher())

################Judy's Code###########################33
#filename: rotcipher.py

# import string

# #letters including and after n produce index out of range
# alp = string.ascii_lowercase*2

# phrase = input('give a phrase for rotation...')
# deg = int(input('give a degree of rotation...'))

# def rot(alp, phrase):
#     modphrase = ''
#     for let in phrase:
#         if let == ' ':
#             modphrase += let
#         modphrase += alp[alp.find(let) + deg]
#     print(modphrase)

# rot(alp, phrase)
        
##########################  HANGMAN  ######################################
'''
Reads the text and return a list of strings which are greater than 5 letters.
Randomly pick a word from that list and begin the game.
Allow the user 10 tries to guess the letters of the word. 
Keep track of the letters the user has already guessed.
Show them a list of 'blanks' and ask them for a letter.
If they guess a letter which is in the word, show the blanks with the letters filled in.
If they guess a letter which is not in the word, tell them and subtract 1 from their remaining guesses. 
If they guess a letter they've guessed before, tell them and do not
 subtract 1 from their guesses.
If the user can't guess the word in the number of allotted guesses, print the word and ask them if they'd like to play again.

'''
#Read file english.txt
# with open('english.txt', 'r') as f:
#     contents = f.read()
# for word in list(contents):
#     print(word)
# print(contents)

# import random


# lineList = list()

# def load_words(path):
#    return [line.rstrip('\n') for line in open('english.txt', 'r') if len(line) > 5]

# def hangman():
#     word_list = load_words('./english.txt') #providing path to filename english
#     return word_list

# def pick_word():
#     random_word = random.choice(hangman())
#     return random_word

# def create_dash():
#     our_random_word = pick_word()
#     dashes = '_ ' * len(our_random_word)
#     print(our_random_word)
#     return dashes

# def compare_user_random():
#     our_random_word = pick_word()
#     print(our_random_word)
#     rounds = 10
#     user_answer = ''
#     #user_answer = ' _ ' * len(our_random_word)
#     while rounds > 0:
#         start=user_answer
#         letter = input('please add letter: ')
#         for char in our_random_word:
#             if char == letter:
#                 start += letter
#             else:
#                 start += ' _ '
#         user_answer=start     
#         print(user_answer)
    
#         rounds -= 1
#     return user_answer

# print(compare_user_random())


########Count Words##############################

'''
Lab21: Count Words
Let's write a python module to analyze a given text file containing a book for its vocabulary frequency and display the most 
frequent words to the user in the terminal. Remember there isn't any "perfect" way to identify a word in english 
(acronymns, mr/ms, contractions, etc), try to find rules that work best.

Find a book on Project Gutenberg. Download it as a UTF-8 text file.

    1. Open the file.
    2. Make everything lowercase, strip punctuation, split into a list of words.
    3. Your dictionary will have words as keys and counts as values. If a word isn't in your dictionary yet, 
       add it with a count of 1. If it is, increment its count.
    4. Print the most frequent top 10 out with their counts. You can do that with the code below.

#word_dict is a dictionary where the key is the word and the value is the count
words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])

Book imported = Dancers in the Dark by Dorothy Speare

'''
# #####################Our Solution 1st Draft##############################
# # count_words.py

# import string

# def count_words(book):
#     punct = str.maketrans("", "", string.punctuation)
#     with open(book, "r") as our_book:
#         contents = our_book.read().lower()
#     contents = contents.replace("\n", "")
#     contents = contents.translate(punct)
#     contents = contents.split(" ")
#     return contents

# result = count_words("dancers_dark_book.txt")
# print(result)
    
# def word_count(contents):
#     book_dict = {}
#     for word in contents:
#         if word not in book_dict:
#             book_dict[word] = 0
#         book_dict[word] += 1
#     return book_dict


# print(word_count(result))

# ####Judy's Solution#########################

# #Filename: wordcount.py

# import string

# with open('ThroughtheDesert.txt', 'r') as f:
#     contents = f.read()

# #print(contents)

# def string_modifier(contents):
#     results = ''
#     contents = contents.lower()
#     for char in contents:
#         if char not in string.punctuation:
#             results += char
#     results = results.split()
#     return results

# result = string_modifier(contents)
# #print(string_modifier(contents))

# def dicreator(result):
#     wdic = {}
#     for word in result:
#         if word not in wdic:
#             wdic[word] = 0
#         wdic[word] +=1
#     return wdic

# wdic = dicreator(result)

# def topten(wdic):
#     words = list(wdic.items())
#     words.sort(key=lambda tup:tup[1], reverse=True)
#     for i in range(min(10,len(words))):
#         print(words[i])

# topten(wdic)


'''
Lab25 ATM
Let's represent an ATM with a class containing two attributes: a balance and an interest rate. 
A newly created account will default to a balance of 0 and an interest rate of 0.1%. Implement the initializer, 
as well as the following functions:

    1. check_balance() returns the account balance
    2. deposit(amount) deposits the given amount in the account
    3. check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative
    4. withdraw(amount) withdraws the amount from the account and returns it
    5. calc_interest() returns the amount of interest calculated on the account






'''
#Classes allow us to write 'methods' or 'member-functions', which are functions that are called 'on the object'.
#They are exactly like regular functions except the first parameter is always 'self'.

#The initializer is a special type of function which uses the parameters passed into it to initialize the instance (of ATM).
#Here, we copy the parameters balance and interestRate into the instance by assigning them variables on self. 
#Self is an object that represents the class "self"

#The variables associated with a class are called 'member variables', 'attributes' or 'fields'.
#The functions associated with the class are called 'methods'
# class ATM:  #declares class called ATM
#     def __init__(self, balance, interestRate):  #this is the initializer, allows us to create instances of the type class
#         self.balance = balance                  #this is a member variable
#         self.interestRate = interestRate        #this is a member variable
#         self.transaction_list = []              #this is a member variable
              

# #TESTING class ATM.  This overides self to test if parameters I am passing are working.  The default value for self is the memory location (000033fsafdaf)
#     def __str__(self):
#         return f'{self.balance} {self.interestRate}'

# #print output    
# an_atm = ATM(0.0, 0.1) #this calls the initializer and instantiate (instantiate = represents an abstraction by a concrete instance)
# print(an_atm)
   
#     ### self is required in ALL methods
#     def check_balance(self): #This is a 'method' or 'member function'.
#         return self.balance

#     def deposit(self, amount):
#         self.balance += amount #taking balance and adding to amount
#         self.transaction_list.append(f'you deposited {amount}')
#         return amount
        
#     def check_withdrawl(self, amount):
#         return self.balance >= amount    # Returns boolean value. If self.balance >= amount = True
    
#     def withdrawl(self, amount):
#         self.balance -= amount
#         self.transaction_list.append(f'you withdrew {amount}')
#         return self.balance    
    
#     def calc_interest(self):  #Do not have enouph info to calculate interest rate
#         pass

#     def print_transactions(self):
#         for transaction in self.transaction_list:
#             print(transaction)

# an_atm = ATM(0.0, 0.1) #INSTIATES variable and creates an object called an_atm. Calling the ATM class and providing it 2 variables for balance and interest rate. 

# #check the initial balance by calling the ATM class and provide the check_balance function with the 2 inherited values
# print(f'Your initial balance is {an_atm.check_balance()}')

# #passing the inheritied variables from the ATM class and adding the deposit
# print(f'You made a deposit for {an_atm.deposit(11)}')  #calling deposit METHOD on the an_atm OBJECT and making deposit of x

# #rechecking the balance
# print(f'Your revised balance is {an_atm.check_balance()}') #calling balance METHOD on the an_atm OBJECT and checing balance 

# #checking to see if check_withdrawl METHOD is working. Will return TRUE if balance is greater than amount
# print(f'Is your balance >= than the withdrawl amount? {an_atm.check_withdrawl(0)}') 

# #passing the inheritied variables from the ATM class and adding a withdrawl
# print(f'You made a withdrawl of {an_atm.withdrawl(500)}') #calling withdrawl METHOD on the an_atm OBJECT and checing balance

# '''
# Part 2: Have the ATM maintain a list of transactions. Every time the user makes a deposit or withdrawal, add a string to a 
# list saying 'user deposited $15' or 'user withdrew $15'. Add a new function print_transactions() to your class for printing 
# out the list of transactions.
# '''
# #def module is part of class
# print(f'You made a deposit for {an_atm.deposit(111)}')
# print(f'You made a withdrawl of {an_atm.withdrawl(0)}')

# '''
# Part3: Allow the user to enter commands into a REPL.

# > what would you like to do (deposit, withdraw, check balance, quit)?
# > deposit
# > how much would you like to deposit?
# > $5
# > what would you like to do (deposit, withdraw, check balance, quit)?
# > check balance
# > balance: $5
# '''

# while True:
#     user_input= input("What would you like to do (deposit, withdraw, check balance or quit?) ")
#     print(f'You chose {user_input}')
            
#     if user_input == 'deposit':
#         amount = int(input('How much would you like to deposit? '))
#         print(f'Thank you for your deposit totaling {an_atm.deposit(amount)}')
    
#     elif user_input == 'withdraw':
#         amount = int(input('How much would you like to withdraw? '))
#         print(f'You made a withdrawl totaling {an_atm.withdrawl(amount)}')
    
#     elif user_input == 'check balance':
#          print(f'Your balance = {an_atm.check_balance()}')

#     elif user_input == 'done':
#          break # Not exiting program. 

'''

Tic Tac Toe  #LAB in progress

'''
# class Player:  #declares class called Player
#     def __init__(self, name, token):             #this is the initializer, allows us to create instances of the type Player
#         self.name =  name                        #this is a member variable
#         self.token = 'X' or 'O'                  #this is a member variable

# class Game:  #declares class called Game
#     def __init__(self, board):                   #this is the initializer, allows us to create instances of the type Game
#         self.board =  [[0]*3]*3
#                               #this is a member variable
#     # def __str__(self):
#     #     print(str(self.board))
        
#     # def create_board(self):
#     #     rows, cols = (3,3)
#     #     arr = [[0]*cols]*rows
#     #     #arr [0][0] =1 #changes the 1st element of the 1st row to x 
#     #     for row in arr:
#     #         print(row)
#     #     return arr
        

# #GET INFO FROM USER AND TELL THE BOARD TO UPDATE ITSELF
#     def move(self, x, y, player):
#         board = []
#         x = self.x
#         y = self.y
#         print(f'{x},{y}')
#         player = self.board
        
#         #print(board)
        
#         return  


# #Create game board
# my_game = Game('Board') #creating an object called my_game. need to asociate the my_game object with Game class
# # (my_game.create_board()) #calling create_board method
    
# #Get user input and assign to board
# player1 =  Player('Ron','X')
# # my_game.move(0, 3, player1)
# print(my_game)


####Testing to see if the Player and Game work##########
# #TESTING class Player.  This overides self to test if parameters I am passing are working.  The default value for self is the memory location (000033fsafdaf)
#     def __str__(self):
#         return f'{self.name} {self.token}'

# #print output    
# a_player = PLAYER('Lolar', 'O') #this calls the initializer and instantiate (instantiate = represents an abstraction by a concrete instance)
# print(a_player) 

# #TESTING class Game.  This overides self to test if parameters I am passing are working.  The default value for self is the memory location (000033fsafdaf)
#     def __str__(self):
#         return f'{self.name}'

# #print output    
# board = GAME('---') #this calls the initializer and instantiate (instantiate = represents an abstraction by a concrete instance)
# print(board)
####Testing to see if the Player and Game work##########
        
'''
Week 3

Lab 20: Credit Card Validation

Let's write a function which returns whether a string containing a credit card number is valid as a boolean. 

The steps are as follows:

    1.Convert the input string into a list of ints
    2.Slice off the last digit. That is the check digit.
    3.Reverse the digits.
    4.Double every other element in the reversed list.
    5.Subtract nine from numbers over nine.
    6.Sum all values.
    7.Take the second digit of that sum.
    8.If that matches the check digit, the whole card number is valid.

For example, the worked out steps would be:

    4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
    4 5 5 6 7 3 7 5 8 6 8 9 9 8 5
    5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
    10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
    1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
    85
    5
    Valid!

'''

# def Convert(string):
#     #user_input = list(string.split(' ')) #converting user input charachter string to a list
#     conversion = [int(x) for x in user_input] #convert number to string, extract each characther and reconvert to integer
#     return conversion 

# def remove_last_digit(credit_card):
#     cc = credit_card[0:15]
#     return cc

# def reverse_digits(credit_card):
#     cc = reversed(credit_card)
#     return cc

# def double_element(credit_card):
#     double_list = {c* 2 for c in credit_card}
#     return double_list

# user_input = input('please enter number ')

# Converted_user_input = Convert(user_input)
# print(Converted_user_input)

# Last_digit_removed = remove_last_digit(Converted_user_input)
# print(Last_digit_removed)

# cc = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
# print(cc)
# cc1 = cc[0:15]
# print(cc1)

# # print(Convert(user_input)) #calling Convert module and providing user_input parameter
# # print(remove_last_digit(user_input)) #calling Convert module and providing user_input parameter

# reverse_cc= reversed(cc1)
# print(reverse_cc)

   
# double_list = {c* 2 for c in cc}
# print(double_list)

# def subtract_nine():
#     pass

# def add_values():
#     pass

# def second_digit_sum():
#     pass

# def match_checkDigit():
#     pass


###### Justin's solution###
# def validat_credit_card(cc_string): #validating length of cc
#     if len(cc_string) !=16:
#         return False

# cc = []
# for i in range(len(cc_string)):
#     cc.append(int(cc_string[i])) #converting text to integer

# check_digit = cc.pop(-1) #removes last digit

# cc_reverse = cc[::-1] #reverses list using slicing 

# for i in range(0, len(cc_reverse, 2)):
#     cc_reverse[i] *=2

# total = 0
# for i in range(len(cc_reverse)):
#     if cc_reverse[i] >9:
#         cc_reverse[i] -=9
#     total += cc_reverse[i]

# second_digit = total %10 #using modulus give 2nd digit

# if check_digit == second_digit:
#     return True
# else:
#     return False

# return cc_reverse

# print(validat_credit_card('1234567890000000'))


'''
Lab 18: Peaks and Valleys

Define the following functions:

1. peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.

2. valleys - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.

3, peaks_and_valleys - uses the above two functions to compile a single list of the peaks and valleys in order of appearance 
in the original data.

'''

# def Peaks(data):
#     peaks_list = []
#     for i in range(1, len(data)-1): #need to define range to 1 and len -1 because it will loop out of range
#         if data[i] > data[i+1] and data[i] > data[i-1]:
#            #print(i)
#             peaks_list.append(i)
#     return peaks_list
    
         
# def Valleys(data):
#     valley_list = []
#     for i in range(1, len(data)-1): #need to define range to 1 and len -1 because it will loop out of range
#         if data[i] < data[i+1] and data[i] < data[i-1]:
#            #print(i)
#             valley_list.append(i)
#     return valley_list
            
# def peaks_and_valleys(peaks,valley):
#  # call the prior functions and add them
#    p = Peaks(data)
#    v = Valleys(data)
   
#    return p + v 
 
# data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]   

# peaks = (Peaks(data))
# #print(peaks)

# valley = (Valleys(data))
# #print(valley)

# peaksValleys = peaks_and_valleys(peaks,valley)
# print(peaksValleys)
  

'''
Lab 18: Peaks and Valleys-Part 2
'''
# # for num in data:
# #     print('x'*num) 

# for num in data:
#     for i in range(num):
#         print('x', end='-')  
#     print()   
    
'''
Lab 15: Number to Phrase

Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.

Hint: you can use modulus to extract the ones and tens digit.

x = 67
tens_digit = x//10
ones_digit = x%10

'''

def number_to_phrase(one,ten):
    pass
   
#print(number_to_phrase(5)) # five


number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#         0      1      2       3       4       5       6       7         8        9
ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

#index     0        1         2         3         4        5        6         7          8          9
tens = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
  
#index     0        1         2         3         4        5        6         7          8          9
teens =  ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen','nineteen' ]


user_input = int(input('enter a number '))  #obtaining user input

ones_digit = user_input%10
tens_digit = user_input//10 #floor division throws away the remainder
teens_digit = user_input%10

print(f'The ones_digit = {ones_digit}')
print(f'The tens_digit = {tens_digit}')

oness = (ones[ones_digit]) #looks at the ones array and uses the ones_digit variable as an index to return value
#print(oness)

tenss = (tens[tens_digit-1])
#print(tenss)

if user_input <=19:
   print(teens[teens_digit-1])
else:
    print(f'You entered {user_input}, which translates to {tenss}-{oness}')
#print(ones[mod_ones])




# print(mod_tens)

#print(ones[user_input])

# user_input_ones = user_input%10
# user_input_tens = user_input//10
# print(user_input_ones)
# print(user_input_tens)

# if user_input_ones 

# print(ones[user_input])
# #print(ones)
# #print(tens)




# #for ones
# for num in range(0,100):
#     if user_input%10 in merged_list:
#         print(merged_list[2])

# #for tens
# for num in range(0,100):
#     if user_input//10 in merged_list:
#         print(merged_list[3])


# print(f'You entered {user_input}')
# print(user_input%10)
# print(user_input//10)










    



