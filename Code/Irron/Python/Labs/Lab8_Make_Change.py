'''
Lab 8: Make Change

Let's convert a dollar amount into a number of coins. The input will be the total amount, the output will be the number of 
quarters, dimes, nickles, and pennies. Always break the total into the highest coin value first, resulting in the fewest amount 
of coins. For this, you'll have to use floor division //, which throws away the remainder. 10/3 is 3.333333, 10//3 is 3.

Concepts Covered

    conditionals, comparisons
    arithmetic

Version 1

Have the user enter the total number in pennies, e.g. for $1.36, the user will enter 136.

Version 2

Have the user enter a dollar amount (1.36), convert this to the total in pennies.

'''
    
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

def all_pennies(dollars):
        no_pennies = round((dollars/.01))
        value_pennies = no_pennies*.01
        #print(dollars,no_pennies, value_pennies)
        print(f'You will recieve {no_pennies} pennies, totaling ${value_pennies}')
        #print(dollars)

        return value_pennies

        
#Part1 ---> obtain user input and returning the number of quarters, dimes, nickels and pennies
# user_input = float(input('Please enter a dollar amount '))
# print()
# dollars = change_quarters(user_input) #$1.42 returns 5 quarters, 1 dime, 1 nickel, 2 pennies
# dollars = change_dimes(dollars) #passing the modulus/remainder from change_quarter to change_dimes
# dollars = change_nickles(dollars) #passing the modulus/remainder from change_dimes to change_nickles
# dollars = change_pennies(dollars) #passing the modulus/remainder from change_nickles to change_pennies

# #Part2 ---> obtan user input and converting to pennies
user_input = float(input('Please enter a dollar amount '))
dollars = all_pennies(user_input) #converts user input to pennies 

# #Part3 ---> obtain user input and allow user to select preferred coins
# def preferred_coin(dollars, coin):
#     if coin == 'pennies':

#start with a till of money, specif amounts for quarters, dimes, nickles, pennies. Randomly pick coins to reduce/update total. 
#ask user preferred denomination, 2 nickles. or 1 dime



