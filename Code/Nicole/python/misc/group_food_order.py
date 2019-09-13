# group_food_order.py

def group_order():
    person = []
    prices = []
    fees = 0.0
    person_total = 0.0
    
    order_total = input("\nWhat is the order total?\n")
    order_total = float(order_total)
    order_total = round(order_total, 2)
    
    while True:
        name = input("\nWhat is your name? (Type 'done' when finished): \n")
        if name == "done":
            break
        person.append(name)
        amount = input("How much is your order?\n")
        prices.append(float(amount))
    
    fee_amount = input("\nHow much is the delivery, tip, and other fees?\n")
    fees =+ float(fee_amount)
    fees = fees / len(prices)
    fees = round(fees, 2)
    
    for i in range(len(prices)):
        prices[i] += fees
    
    for j in range(len(prices)):
        person_total += prices[j]
    
    print(f"\nThe order total is ${order_total} and the group total is ${person_total}")
    
    if abs(person_total - order_total) > .03:
        print("\nUh, oh. Something's wrong, your numbers don't add up.")
        exit()
    
    for x in range(len(person)):
        print(f"\n{person[x]}, your total is ${prices[x]}.")
    
    return print("\nEnjoy your meal!\n")

group_order()