'''
Lab 15: Number to Phrase

Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.

Hint: you can use modulus to extract the ones and tens digit.

x = 67
tens_digit = x//10
ones_digit = x%10

Hint 2: use the digit as an index for a list of strings.
Version 2

Handle numbers from 100-999.

'''
def calc_ones_place(number): 
    
    oneslist = []
    tenslist = []
    hundredslist =[]
        
    oneslist.append(number%10)
    tenslist.append(number//10%10) #---> taking the modulus of the floor. so floor of 789 = 78 and modulus of 78 = 8
    hundredslist.append(number//100)

    
    ones = {'': ' ',
            0 :'zero',
            1 : 'one', 
            2 : 'two', 
            3 : 'three', 
            4 : 'four', 
            5 : 'five', 
            6 : 'six', 
            7 : 'seven',
            8 : 'eight',
            9 : 'nine' ,   }  

    tens = {'': ' ',
            0 :'zero',
            1 : 'ten', 
            2 : 'twenty', 
            3 : 'thirty', 
            4 : 'forty', 
            5 : 'fifty', 
            6 : 'sixty', 
            7 : 'seventy',
            8 : 'eighty',
            9 : 'ninety' ,   } 
 
    hundreds = {1 : 'one-hundred',
                2 : 'two-hundred',
                3 : 'three-hundred',
                4 : 'four-hundred',
                5 : 'five-hundred',
                6 : 'six-hundred',
                7 : 'seven-hundred',
                8 : 'eight-hundred',
                9 : 'nine-hundred',}

    print(f'You typed {number}')
    print(f'The hundreds digit = {hundredslist}, tens digit = {tenslist}, ones digit = {oneslist}') #--->returns numbers in a list
    print(f'The hundreds digit = {hundredslist[0]}, tens digit = {tenslist[0]}, ones digit = {oneslist[0]}') #---> returns actual values within list
    
    #Assigning values from dictionary ...REVIEW>>>
    ones_digit = ones[oneslist[0]] #---> retrieving values from dictionary by using values from list as keys 
    tens_digit = tens[tenslist[0]]
    hundreds_digit = hundreds[hundredslist[0]]
    print(f'The text translation for number {number} = {hundreds_digit} {tens_digit} {ones_digit}')

    return 

 


user_input = int(input('Please enter a number '))
#print(user_input)
ones_digit = calc_ones_place(user_input)
print(ones_digit)



#Msc Code

#hundreds_check = int((number//100))
    # print(f'Hundreds place = {hundreds_check}')
 #if hundreds_check == 0:
        #---> Evaluating if number is between 0 and 99. 
        #oneslist.append(number%10) #--->using modulus to find ones digit and append to list. modulus returns the remainder. 
        #numberslist.append(number%10)
        #ones_digit = ones[oneslist[0]] #---> accessing the values in the ones dictionary by using index onelist list 
        #print(f'The ones digit = {ones_digit}')

        #tenslist.append(number//10) #---> using floor division to find the tens digit. floor division disgards the remainder and returns the integer
        #numberslist.append(number//10)
        #tens_digit = ones[tenslist[0]]
        #print(f'The tens digit = {tens_digit}')

        #print(f'Number translation to words = {tens_digit} {ones_digit} ')
        
    #if hundreds_check > 0:
        #hundredslist.append((number//100)) #---> using floor division to find the hundreds digit. floor division disgards the remainder and returns the integer
        #numberslist2.append(number//100)
        #print(hundredslist)
        #hundreds_digit = hundreds[hundredslist[0]] #---> using the number in hundreds place as a key to find value. 
        #print(f'The hundreds digit = {hundreds_digit}')
    
    #print(f'Total translation = {hundreds_digit} {tens_digit} {ones_digit}')
    #print(numberslist)
        
        #return hundreds_digit, tens_digit, ones_digit
        #APPEND words in a list and print list ??
    
        
    
    #print(f'Number translation to words = {hundreds_digit } {tens_digit} {ones_digit} ')


    #Next steps: check code for hundreds place. maybe not liking floor division for 100.  address zero value for digits 1 thru 9
    


    # if ' ' in tens_digit:
    #     tens_digit(strip()) #---> removing the blank space for digits 1 thru 9, otherwise blank space will be interpreted as 0 and returns zero, resulting in zero9 for the number 9




# ones_place = ones[9]
# print(ones)
# print (ones_place)

# modulus = 68%10
# dict_value = ones[modulus]
# print(f'value from dictionary = {dict_value}')

# for o in ones.values():
#     print(ones[67%10])


#take user value, convert to number, takes the units place and check against each value of dictionary