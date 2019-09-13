

total = float(input('What is your total amount: '))
quarters = .25
dimes = .10
nickels = .05
pennies = .01


# print('=====')
# print(.03//.01)f
# print(.03/.01)
#
# print('======')
ff

def makechange(total):

    quarters_back = total // quarters
    total -= quarters_back * quarters
    dimes_back = total // dimes
    total -= dimes_back * dimes
    nickels_back = total // nickels
    total -= nickels_back * nickels
    pennies_back = round(total / pennies)
    total -= pennies_back * pennies + 1



    print(f'Quarters = {quarters_back}')
    print(f'Dimes = {dimes_back}')
    print(f'Nickels = {nickels_back}')
    print(f'Pennies = {pennies_back}')
    print(quarters_back*quarters + dimes_back*dimes + nickels_back*nickels + pennies_back*pennies)


    # partial to
    # dimes = total // .10
    # print(quarters)
    # print(dimes)
makechange(total)
