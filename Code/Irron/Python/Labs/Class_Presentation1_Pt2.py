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
        print(f'The remaining ${modulus} cents will be donated to your favorite charity!')

    #allocating full balance to dimes
    elif 'dimes' in coin_split:
        no_dimes = int(amount/.10)
        value_dimes = no_dimes*.10
        modulus = amount%.10
        print(f'You will recieve {no_dimes} dimes(s), totaling ${value_dimes}')
        print(f'The remaining ${modulus} cents will be donated to your favorite charity!')

    #allocating full balance to quarters
    elif 'quarters' in coin_split:
        no_quarters = int(amount/.25)
        value_quarters = no_quarters*.25
        modulus = amount%.25
        print(f'You will recieve {no_quarters} quarters(s), totaling ${value_quarters}')
        print(f'The remaining ${modulus} cents will be donated to your favorite charity!')
  
  
    #print(amount, preference)

#Calling Functions ---> obtan user preference and convert to single coin denomination  
user_input = float(input('Please enter a dollar amount $ '))
user_preference = input(f'How would you like to receive the ${user_input}? (Type 1 denomination: quarters, dimes, nickles, or pennies) ')
print()
#print(user_preference)
preference = calc_single_preference(user_input, user_preference)

'''Part2 Single Coin Disbursement*****************************************************Part2*******************************************************************Part2** '''
