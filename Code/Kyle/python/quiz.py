def quiz():
    count = 0
    user_input = input("What is Kyles favorite color? Red, Green, or Blue")
    if user_input == "Green".lower():
        print("Correct!")
        count += 1
        print(f'Your score: {count}')
    else:
        print("Incorrect")
        count += 0
        print(count)

    user_input = input("Favorite car? Camaro, Mustang, other...")
    if user_input == "Camaro".lower():
        print("Correct!")
        count += 1
        print(f'Your score: {count}')


quiz()
