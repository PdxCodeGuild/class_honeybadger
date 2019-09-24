
'''Part 4 Calculating & Interpreting Exchange Rates*************************************************************Part4*******************************************************************Part4*****'''

def compute_exchange(exchange):
    
    exchange_rate = {'EUR' :0.90990, #Euro
                     'GBP' :0.80435, #British Pound
                     'CAD' :1.32609, #Canadian Dollar
                     'INR' :70.7430, #Indian Rupee
                     'MXN' :19.4841, #Mexican Peso
                     'AUD' :1.47611  } #Australlian Dollar

    if exchange == 'EUR':
        rate_eur = exchange_rate['EUR']
        eur_usd = (1/rate_eur) #---> inversing rate, cost to buy one EUR using U.S. dollars
        print(f'You entered the {exchange} currency.  The USD/{exchange} rate is {rate_eur}.  This means it costs {rate_eur} euros for 1 U.S. dollar.')
        print(f'Interpreted as, how much it will cost to buy one U.S. dollar using euros.')
        print()
        print(f'The {exchange}/USD rate is ${eur_usd}. It will cost ${eur_usd} U.S. dollars to buy one euro.')
        
    
    elif exchange == 'GBP':
        rate_gbp = exchange_rate['GBP']
        gbp_usd = (1/rate_gbp)
        print(f'You entered the {exchange} currency.  The USD/{exchange} rate is {rate_gbp}.  This means it costs {rate_gbp} British pounds for 1 U.S. dollar.')
        print(f'Interpreted as, how much it will cost to buy one U.S. dollar using British pounds.')
        print()
        print(f'The {exchange}/USD rate is ${gbp_usd}. It will cost ${gbp_usd} U.S. dollars to buy one British pound.')
    
    elif exchange == 'CAD':
        rate_cad = exchange_rate['CAD']
        cad_usd = (1/rate_cad)
        print(f'You entered the {exchange} currency.  The USD/{exchange} rate is {rate_cad}.  This means it costs {rate_cad} Canadian dollars for 1 U.S. dollar.')
        print(f'Interpreted as, how much it will cost to buy one U.S. dollar using Canadian dollars.')
        print()
        print(f'The {exchange}/USD rate is ${cad_usd}. It will cost ${cad_usd} U.S. dollars to buy one Canadian dollar.')
    
    
    elif exchange == 'INR':
        rate_inr = exchange_rate['INR']
        inr_usd = (1/rate_inr)
        print(f'You entered the {exchange} currency.  The USD/{exchange} rate is {rate_inr}.  This means it costs {rate_inr} Indian Rupees for 1 U.S. dollar.')
        print(f'Interpreted as, how much it will cost to buy one U.S. dollar using Indian rupees.')
        print()
        print(f'The {exchange}/USD rate is ${inr_usd}. It will cost ${inr_usd} U.S. dollars to buy one Indian rupee.')
    
    elif exchange =='MXN':
        rate_mxn = exchange_rate['MXN']
        mxn_usd = (1/rate_mxn)
        print(f'You entered the {exchange} currency.  The USD/{exchange} rate is {rate_mxn}.  This means it costs {rate_mxn} Mexican pesos for 1 U.S. dollar.')
        print(f'Interpreted as, how much it will cost to buy one U.S. Dollar using Mexican pesos.')
        print()
        print(f'The {exchange}/USD rate is ${mxn_usd}. It will cost ${mxn_usd} U.S. dollars to buy one Mexican peso.')
    
    elif exchange == 'AUD':
        rate_aud = exchange_rate['AUD']
        aud_usd = (1/rate_aud)
        print(f'You entered the {exchange} currency.  The USD/{exchange} rate is {rate_aud}.  This means it costs {rate_aud} Australlian dollar for 1 U.S. dollar.')
        print(f'Interpreted as, how much it will cost to buy one U.S. dollar using Australlian dollars.')
        print()
        print(f'The {exchange}/USD rate is ${aud_usd}. It costs ${aud_usd} U.S. dollars to buy one Australlian dollar.')
    
    else:
        print('Please Enter Correct International Currency')
        print()

    
    #print(exchange_rate)
    print()
    print('Rates reflected as of 2019-09-23 9:47 PST. Rates retrieved from https://www.xe.com/')
    return exchange_rate


#Calling Function
print()
user_input = input('Please enter currency (EUR, GBP, CAD, INR, MXN, AUD)' )
print()
#print(user_input)
compute_exchange(user_input)

'''Part 4 Calculating & Interpreting Exchange Rates*************************************************************Part4*******************************************************************Part4*****'''


               