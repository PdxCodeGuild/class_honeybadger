import random
​
print(("*"*10) + "Welcome to the Gambling Calculator Game" + ("*"*10))
​
# variables
num1 = 0
num2 = 0
score = 0
round_num = 1
play_again = "y"
operators_list = ["+", "-", "*", "/"]
​
chosen_operator = ""
​
while play_again == "y":
    num1 = int(input("Give me a number: "))
    num2 = int(input("Give me another number: "))
​
    chosen_operator = random.choice(operators_list)
​
    print(f"Round {round_num}")
    print(f"{num1} {chosen_operator} {num2}")
​
    if chosen_operator == "+":
        results = num1 + num2
    elif chosen_operator == "-":
        results = num1 - num2
    elif chosen_operator == "*":
        results = num1 * num2
    else:
        results = num1 / num2
​
    score += results
    print(f"Results for this round: {results}")
    print(f"Overall score: {score}")
​
    play_again = input("Do you want to play again? (y/n)").lower()
​
    while play_again not in ["y", "n"]:
        play_again = input("Do you want to play again? (y/n)").lower()
​
else:
    print(f"Goodbye. Your final score is {score}.")
