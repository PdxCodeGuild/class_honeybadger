#filename: guess_the_number.py

#modules
import random

#set of 1 to 10
numbers=[1,2,3,4,5,6,7,8,9,10]

#greetings
print("Hello, you will get 10 tries to guess the number between 1 and 10...."" Lets see if you can do it :)")

#number chosen at random by pc
pc_num=random.choice(numbers)

#user input defined as a variable to set up while loop ensuring proper inputs
usr_num=1

#guess tracker
attempts=0

#user inputs a number between 1 and 10
while attempts<10:

    while 1 <= usr_num <= 10:
        attempts+=1
        try:
            usr_num=int(input("Choose a number between 1 and 10 "))
            print("That's attempt number ",attempts)

            if usr_num<1 or usr_num>10:
                print("Between 1 and 10, please...")
                if usr_num!=pc_num:
                    if usr_num>pc_num:
                        print("Too high.")
                    elif usr_num<pc_num:
                        print("Too low.")

                    print("try again! ")
                    usr_num=int(input("Choose a number between 1 and 10 "))

                else:
                    print("The chosen number was ",pc_num,"You won in ", attempts,"guesses")
                    break

        except ValueError:
            print("Please enter a number you rascal... ")

            print("Thats ",attempts," guesses so far")


    else:

        print("usr_num outside acceptable range")
        break

else:
    print("That's ten guesses pardner! yer OUTTA LUCK")
#display random number
print("the randomly chosen number was", pc_num)
