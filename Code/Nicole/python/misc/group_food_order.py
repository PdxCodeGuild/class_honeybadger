# group_food_order.py

def group_order():
    person = []
    prices = []
    fees = 0.0
    person_total = round(0.0)
    discounts = 0.00
    
    order_total = input("\nWhat is the order total, including delivery and tip?\n")
    order_total = float(order_total)
    order_total = round(order_total, 2)
    
    while True:
        name = input("\nWhat is your name? (Type 'done' when finished): \n")
        if name == "done":
            break
        person.append(name)
        first_item = "yes"
        amount = 0
        while first_item == "yes":
            amount_input = input("How much is your food item?\n")
            amount_input = float(amount_input)
            amount_input = round(amount_input, 2)
            split = input("Did you split this order with someone? Type 'yes' or 'no': \n")
            if split == "yes":
                split_num = input("How many people split this item? \n")
                split_num = float(split_num)
                split_amount = amount_input / split_num
                split_amount = round(split_amount, 2)
                amount += split_amount
            else:
                amount += round(amount_input, 2)
            first_item = input("Do you have another item? Please type 'yes' or 'no': \n")
        amount = round(amount, 2)
        prices.append(float(amount))
    
    
    
    fee_amount = input("\nHow much is the delivery, tip, and other fees?\n")
    fees =+ float(fee_amount)
    fees = fees / len(prices)
    fees = round(fees, 2)
    
    for i in range(len(prices)):
        prices[i] += fees
    
    for j in range(len(prices)):
        person_total += prices[j]
    
    discount_input = input("\nWere any discounts applied to the order?\n")
    if discount_input == "yes":
        discount = input("\nHow much was the discount? ")
        discount = float(discount)
        discount = round(discount, 2)        
        for k in range(len(prices)):
            prices[k] -= float(discount / len(prices))
    
    order_total -= discount
    
    print(f"\nThe order total is ${order_total} and the group total is ${person_total}")
    
    if abs(person_total - order_total) > .05:
        print("\nUh, oh. Something's wrong, your numbers don't add up.")
        # exit()
    
    for x in range(len(person)):
        print(f"\n{person[x]}, your total is ${prices[x]}.")
    
    return print("\nEnjoy your meal!\n")

group_order()