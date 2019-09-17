# lab_19_blackjack_advice.py

# URL :: https://github.com/PdxCodeGuild/class_honeybadger/blob/master/1%20Python/labs/lab19-blackjack_advice.md

def blackjack_advice():
    blackjack_dict = {
        "A" : 1,
        "2" : 2,
        "3" : 3,
        "4" : 4,
        "5" : 5,
        "6" : 6,
        "7" : 7,
        "8" : 8,
        "9" : 9,
        "10" : 10,
        "J" : 10,
        "Q" : 10,
        "K" : 10
        }
    
    card_value = 0
    play_rounds = ["first", "second", "third"]
    result = ""
    
    for i in range(len(play_rounds)):
        user_play = input(f"What's your {play_rounds[i]} card? ").upper()
        card_value += blackjack_dict[user_play]
    if card_value < 17:
        result = "Hit"
    elif card_value >= 17 and card_value < 21:
        result = "Stay"
    elif card_value == 21:
        result = "Blackjack!"
    elif card_value > 21:
        result = "Already busted"
    
    return f"{card_value} — {result}"
    
print(blackjack_advice())