'''
Present make change lab. Add function for preferred coins..all quarters, all dimes, no pennies
Add foreign exchange component. Convert pesos to dollar to get change. and dollars to get pesos...hold intl values in dictionary??
Submit in Powerpoint..get rid of those damn pennies..donate them to charity

reason for selecting lab = 1st lab that gave me a headache (during intr class). to attempt to solve the lab in 2 weeks with 
a better understanding of python concetps was extreml satisfying 


Class Presentation: Extension of Lab8_Make Change

Part1: Converting a dollar amount into a number of coins. The input will be the total amount, the output will be the number of 
quarters, dimes, nickles, and pennies. Always break the total into the highest coin value first, resulting in the fewest amount 
of coins. For this, you'll have to use floor division //, which throws away the remainder. 10/3 is 3.333333, 10//3 is 3.

Part2: Coverting users preferred coins, (single coins). 

Part3: Coverting users preferred coins, (multiple coins).  Found all combinations of coins

Part3: Converting international coins.

Challenges : had to break single/multiple into seperate functions (wasnt recognizing multiple preferences, going to single)
---> didnt need to append, used split
---> if 'quarters' in coin_split and 'dimes' in coin_split vs if 'quarters' and 'dimes' in coin_split

'''

''' *Part1 Full Coin Disbursement****************************************************Part1***************************************************************Part1************'''    
def change_quarters(dollar):
    change = dollar
    if dollar%.25 == 0:
        no_quarters = dollar/.25
        value_quarters = no_quarters *.25
        modulus = dollar%.25
        change = change - value_quarters
        print(f'You deposited ${dollar}.  You will receive {no_quarters} quarters')
        print()

    elif dollar%.25 != 0:
        change = dollar
        no_quarters = int(dollar/.25)
        value_quarters = no_quarters *.25
        modulus = dollar%.25
        change = dollar - value_quarters
        #print(dollar, no_quarters, value_quarters, modulus)
        print(f'You deposited ${dollar}.  You will receive {no_quarters} quarters and the remaining {modulus} will be disbured in either dimes, nickles or pennies.')
        # print(change)
        # print(dollar)
        # print(modulus)
        print()

    return modulus

#allocating balance to dimes    
def change_dimes(dollars):
    no_dimes = int(dollars/.10)
    value_dimes = no_dimes*.10
    modulus = dollars%.10
    print(f'Balance to be disbursed in coins = {dollars}, No. dimes = {no_dimes}, Value of dimes = {value_dimes}, Further disbursement = {modulus}.')
    print(f'You will also recieve {no_dimes} dime(s) and the remaining {modulus} will be dispersed in nickles and pennies.')
    print()
    return modulus

#allocating balance to nickles
def change_nickles(dollars):
    no_nickles = int(dollars/.05)
    value_nickles = no_nickles*.05
    modulus = dollars%.05
    print(f'Balance to be disbursed in coins = {dollars}, No. nickles = {no_nickles}, Value of nickles = {value_nickles}. Further disbursmenent = {modulus}')
    print(f'You will also recieve {no_nickles} nickles(s) and the remaining {modulus} will be dispersed in pennies.')
    print()
    return modulus

#allocating balance to pennies
def change_pennies(dollars):
    no_pennies = round((dollars/.01))
    value_pennies = no_pennies*.01
    modulus = dollars%.01
    #print(dollars, no_pennies, value_pennies, modulus)
    print(f'Balance to be disbursed in coins = {dollars}, No. pennies = {no_pennies}, Value of pennies = {value_pennies}. Further disbursmenent = {modulus}')
    print(f'With the final disbursment, you will receive {no_pennies} pennies(s) with {modulus} remaining to for allocation. ')
    print()
    return modulus

##Calling Functions ---> obtain user input and returning the number of quarters, dimes, nickels and pennies
# user_input = float(input('Please enter a dollar amount '))
# print()
# dollars = change_quarters(user_input) #$1.42 returns 5 quarters, 1 dime, 1 nickel, 2 pennies
# dollars = change_dimes(dollars) #passing the modulus/remainder from change_quarter to change_dimes
# dollars = change_nickles(dollars) #passing the modulus/remainder from change_dimes to change_nickles
# dollars = change_pennies(dollars) #passing the modulus/remainder from change_nickles to change_pennies

'''*Part1 Full Coin Disbursement***************************************************Part1*******************************************************************Part1*******'''

'''Part2 Single Coin Disbursement*****************************************************Part2*******************************************************************Part2** '''

def calc_single_preference(amount, preference):
    coin_split = preference.split(', ') #--->splitting user preferences by comma and space. split returns results in a list
    #print(coin_split)
    
    #allocating full balance to pennies
    if 'pennies' in coin_split:
        no_pennies = round((amount/.01))
        value_pennies = no_pennies*.01
        #print(amount,no_pennies, value_pennies)
        print(f'You will recieve {no_pennies} pennies, totaling ${value_pennies}')
        #print(amount)
        
    #allocating full balance to nickles
    elif 'nickles' in coin_split:
        no_nickles = int(amount/.05)
        value_nickles = no_nickles*.05
        modulus = amount%.05
        print(f'You will recieve {no_nickles} nickle(s), totaling ${value_nickles}')
        print(f'The remaining {modulus} cents will be donated to your favorite charity')

    #allocating full balance to dimes
    elif 'dimes' in coin_split:
        no_dimes = int(amount/.10)
        value_dimes = no_dimes*.10
        modulus = amount%.10
        print(f'You will recieve {no_dimes} dimes(s), totaling ${value_dimes}')
        print(f'The remaining {modulus} cents will be donated to your favorite charity')

    #allocating full balance to quarters
    elif 'quarters' in coin_split:
        no_quarters = int(amount/.25)
        value_quarters = no_quarters*.25
        modulus = amount%.25
        print(f'You will recieve {no_quarters} quarters(s), totaling ${value_quarters}')
        print(f'The remaining {modulus} cents will be donated to your favorite charity')
  
  
    #print(amount, preference)

##Calling Functions ---> obtan user preference and convert to single coin denomination  
# user_input = float(input('Please enter a dollar amount '))
# user_preference = input(f'How would you like the ${user_input} returned? (quarters, nickles, dimes, or pennies) ')
# print()
# #print(user_preference)
# preference = calc_single_preference(user_input, user_preference)

'''Part2 Single Coin Disbursement*****************************************************Part2*******************************************************************Part2** '''

'''Part 3 Multiple Coin Disbursement*************************************************************Part3*******************************************************************Part3*****'''
def preferred_coin(amount, preference):
    coin_split = preference.split(', ') #--->splitting user preferences by comma and space. split returns results in a list
    print(coin_split)
    #               0           1       2           3
    coinlist = ['quarters', 'dimes', 'nickles', 'pennies']

     # #allocating full balance to quarters and dimes
    if all((c in coinlist for c in ['quarters', 'dimes'])): #---> for each element in qtr_dime, check if elements exist in coin_split
    
        no_quarters = int(amount/.25)
        value_quarters = no_quarters*.25
        modulus = amount%.25
        no_dimes = int(modulus/.10)
        value_dimes = no_dimes*.10
        print(f'You will recieve {no_quarters} quarters(s) and {no_dimes} dimes(s) totaling ${(value_quarters+value_dimes)}')
        #print(f'The remaining {modulus} cents will be donated to your favorite charity')
       
    #allocating full balance to quarters and nickles
    elif all((c in coinlist for c in ['quarters', 'nickles'])): #---> for each element in qtr_dime, check if elements exist in coin_split
    
        no_quarters = int(amount/.25)
        value_quarters = no_quarters*.25
        modulus = amount%.25
        no_nickles = int(modulus/.05)
        value_nickles = no_nickles*.05
        print(f'You will recieve {no_quarters} quarters(s) and {no_nickles} nickle(s) totaling ${(value_quarters+value_nickles)}')
        #print(f'The remaining {modulus} cents will be donated to your favorite charity')


    #allocating full balance to dimes and nickles
    elif all((c in coinlist for c in ['dimes', 'nickles'])): #---> for each element in qtr_dime, check if elements exist in coin_split
    
        no_dimes = int(amount/.10)
        value_dimes = no_dimes*.10
        modulus = amount%.10
        no_nickles = int(modulus/.05)
        value_nickles = no_nickles*.05
        print(f'You will recieve {no_dimes} dimes(s) and {no_nickles} nickle(s) totaling ${(value_dimes+value_nickles)}')
        #print(f'The remaining {modulus} cents will be donated to your favorite charity')
    
    print(amount, preference)
    
    

  
#  if 'pennies' and 'dimes' in coin_split:
              
#         print('true') 
#     else:
#         print('false')     



#qtr_nickel = ['quarters', 'nickels']
    #qtr_dime = ['quarters', 'dimes']


        
    
#allocating full balance to quarters and dimes
    if 'quarters' in coin_split and 'dimes' in coin_split: 
        no_quarters = int(amount/.25)
        value_quarters = no_quarters*.25
        modulus = amount%.25
        no_dimes = int(modulus/.10)
        value_dimes = no_dimes*.10
        balance = modulus
        print(f'You will recieve {no_quarters} quarters(s) and {no_dimes} dimes(s) totaling ${(value_quarters+value_dimes)}')
        print(f'The remaining change will be donated to your favorite charity')
       
#     #allocating full balance to quarters and nickles
#     elif 'quarters'in coin_split and 'nickles' in coin_split:
#         no_quarters = int(amount/.25)
#         value_quarters = no_quarters*.25
#         modulus = amount%.25
#         no_nickles = int(modulus/.05)
#         value_nickles = no_nickles*.05
#         print(f'You will recieve {no_quarters} quarters(s) and {no_nickles} dimes(s) totaling ${(value_quarters+value_nickles)}')
#         print(f'The remaining change will be donated to your favorite charity') 
  
    
#    #allocating full balance to dimes and nickles
#     elif 'quarters'in coin_split and 'nickles' in coin_split:
#         no_dimes = int(amount/.10)
#         value_dimes = no_dimes*.10
#         modulus = amount%.10
#         no_nickles = int(modulus/.05)
#         value_nickles = no_nickles*.05
#         print(f'You will recieve {no_quarters} quarters(s) and {no_nickles} dimes(s) totaling ${(value_quarters+value_nickles)}')
#         print(f'The remaining change will be donated to your favorite charity') 
    
        

# result =  all(elem in coinlist for elem in coin_split) #---> for each element in qtr_dime, check if elements exist in coin_split
#     if result:
#         no_quarters = int(amount/.25)
#         value_quarters = no_quarters*.25
#         modulus = amount%.25
#         no_dimes = int(modulus/.10)
#         value_dimes = no_dimes*.10
#         print(f'You will recieve {no_quarters} quarters(s) and {no_dimes} dimes(s) totaling ${(value_quarters+value_dimes)}')
#         print(f'The remaining {modulus} cents will be donated to your favorite charity')




##Calling Functions ---> obtan user preference and convert to multiple coin denominations
user_input = float(input('Please enter a dollar amount $'))
user_preference = input(f'How would you like the ${user_input} returned? (quarters, nickles, dimes, pennies) ')
print()
#print(user_preference)
preference = preferred_coin(user_input, user_preference)

# #Part3 ---> obtain user input and allow user to select preferred coins
# 

#start with a till of money, specif amounts for quarters, dimes, nickles, pennies. Randomly pick coins to reduce/update total. 
#ask user preferred denomination, 2 nickles. or 1 dime










