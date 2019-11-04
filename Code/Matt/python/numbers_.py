# import random
# play_again = "yes"
# counter = 0
# computer_choice = random.randint(1,10)
# print(computer_choice)
# while play_again == "yes" and counter < 11 :
#     counter += 1
#     print(f"round {counter}")
#     guess = input("Hello, guess a number from (1-10)")
#     if guess.isdigit():
#         guess = int(guess)
#     else:
#         print("enter a number!")
#
#
#     if computer_choice == guess:
#         print(f"you nailed it in {counter} times")
#     elif computer_choice > guess:
#         print("try a lower number ")
#     else:
#         print("try a higher number")
#
#     play_again = input("Do you want to play again?")
# else:
#     print("goodybe")
