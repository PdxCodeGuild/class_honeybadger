
Q = 10
K = 10
A = 1
J = 10



user_hand1 = float(input("Whats your first card? "))
user_hand2= float(input("Whats your second card? "))
user_hand3 = float(input("Whats your third card? "))

hand_sum = [user_hand1, user_hand2, user_hand3]

def add_user_hand():
    added = sum(hand_sum)
    return added
    print(added)

add_user_hand()


# def card_value():
#     if user_input == "A":
#         return 1
#     elif user_input == "K":
#         return 10
#     elif user_input == "Q":
#         return 10
#     elif user_input == "J":
#         return 10

# card_value()
