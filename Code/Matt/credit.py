card_number = list(input('Enter your 16 digit credit card number: '))

# turns the list into integers
for i in range(len(card_number)):
    card_number[i] = int(card_number[i])

# grabs the last digit
check_digit = card_number[-1:]

# a list without the last digit
card_number = card_number[0:-1]

# reverses the card_number list
card_number.reverse()

# multiplies every other index by 2
def list_muliplier(a_list):
    for i in range(len(card_number)):
        if i % 2 == 0:
            card_number[i] = card_number[i]*2
    return card_number

# takes the list and subtracts 9 from values greater than 9
def nine (a_list):
    for i in range(len(card_number)):
#  got extremely stuck here:
        if card_number[i] > 9:
          card_number[i] -= 9
    return card_number
# grabs the sum of the list
sum_of_card_number = sum(card_number)
sum_of_card_number = [int(i) for i in str(sum_of_card_number)]
sum_of_card_number = sum_of_card_number[-1:]
if sum_of_card_number == check_digit:
    print('Your card number is valid')
else:
    print('Your card number is invalid')

list_muliplier(card_number)
nine(card_number)
