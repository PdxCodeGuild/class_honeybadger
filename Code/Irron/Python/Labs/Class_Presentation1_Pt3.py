'''Part 3 Multiple Coin Disbursement*************************************************************Part3*******************************************************************Part3*****'''
def preferred_coin(amount, preference):
    coin_split = preference.split(', ') #--->splitting user preferences by comma and space. split returns results in a list
    #print(coin_split)
    #               0           1       2           3
    coinlist = ['quarters', 'dimes', 'nickles', 'pennies']

     # #allocating full balance to quarters and dimes
    if all((c in coin_split for c in ['quarters', 'dimes'])): #---> checking if quarters and dimes are equal to user_input
    
        no_quarters = int(amount/.25)
        value_quarters = no_quarters*.25
        modulus = amount%.25
        quarter_modulus_to_dimes = modulus%.10
        no_dimes = int(modulus/.10)
        value_dimes = no_dimes*.10
        print(f'You will recieve {no_quarters} quarters(s) and {no_dimes} dimes(s) totaling ${(value_quarters+value_dimes)}')
        print(f'The remaining {quarter_modulus_to_dimes} cents will be donated to your favorite charity!')
       
    #allocating full balance to quarters and nickles
    elif all((c in coin_split for c in ['quarters', 'nickles'])): #---> for each element in qtr_dime, check if elements exist in coin_split
    
        no_quarters = int(amount/.25)
        value_quarters = no_quarters*.25
        modulus = amount%.25
        quarter_modulus_to_nickles = modulus%.05
        no_nickles = int(modulus/.05)
        value_nickles = no_nickles*.05
        print(f'You will recieve {no_quarters} quarters(s) and {no_nickles} nickle(s) totaling ${(value_quarters+value_nickles)}')
        print(f'The remaining {quarter_modulus_to_nickles} cents will be donated to your favorite charity!')


    #allocating full balance to dimes and nickles
    elif all((c in coin_split for c in ['dimes', 'nickles'])): #---> for each element in qtr_dime, check if elements exist in coin_split
    
        no_dimes = int(amount/.10)
        value_dimes = no_dimes*.10
        modulus = amount%.10
        dime_modulus_to_nickles = modulus%.05
        no_nickles = int(modulus/.05)
        value_nickles = no_nickles*.05
        print(f'You will recieve {no_dimes} dimes(s) and {no_nickles} nickle(s) totaling ${(value_dimes+value_nickles)}')
        print(f'The remaining ${dime_modulus_to_nickles} cents will be donated to your favorite charity!')
        print()
    
    #print(amount, preference)
    
    

##Calling Functions ---> obtan user preference and convert to multiple coin denominations
user_input = float(input('Please enter a dollar amount $'))
user_preference = input(f'How would you like the ${user_input} returned? (quarters, nickles or dimes) ')
print()
#print(user_preference)
preference = preferred_coin(user_input, user_preference)

'''Part 3 Multiple Coin Disbursement*************************************************************Part3*******************************************************************Part3*****'''

# Msc Code...NOT WORKING....UUUGHHHHHH!!!
# allocating full balance to quarters and dimes
#     if 'quarters' in coin_split and 'dimes' in coin_split: 
#         no_quarters = int(amount/.25)
#         value_quarters = no_quarters*.25
#         modulus = amount%.25
#         no_dimes = int(modulus/.10)
#         value_dimes = no_dimes*.10
#         balance = modulus
#         print(f'You will recieve {no_quarters} quarters(s) and {no_dimes} dimes(s) totaling ${(value_quarters+value_dimes)}')
#         print(f'The remaining change will be donated to your favorite charity')
       
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