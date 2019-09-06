

card_number = [4, 5, 4, 3, 2, 1, 5, 3, 5, 3, 4, 3, 5, 7, 4, 9]
check_digit = 9


card_number.pop(-1)
list.reverse(card_number)

print(card_number)
print(check_digit)

new_card_number = []

for i in range(0, len(reversed-card_number)):
    new_card_number.append(int(card_number[i]))
    new_card_numberreversed[i] *= 2

total = 0 
for i in range(len(reversed_card_number)):
    if reversed_card_number[i] > 9:
        reversed_card_number[i] -= 9
    total += reversed_card_number[i]

    second_digit = total % 10

if second_digit == check_digit:
    return True
else: 
    return False









    
    

    
    




    
    



