# user greeting
print("Welcome to your MadLibs!\n")

repeat = int(repeat)
yes = 1
no = 0

#variable =
thing1 = input("Name a thing (plural): ")
animal = input("Name an animal: ")
vehicle = input("Name a vehical: ")
places = input("Name a place: ")
verb = input("Name a verb: ")
thing2 = input("Name a thing (plural): ")
adj = input("Name an adjective: ")

story = (f"Dashing through the {thing1}\nIn a one {animal} open {vehicle}\nO'er the {places} we go\nLaughing all the way\nBells on bob tails {verb}\nMaking {thing2} bright\nWhat fun it is to laugh and sing\nA {adj} song tonight\n\n")

#fstring: prints variables inside strings
print(f"{story}")
print("Thanks for playing MadLibs!")

repeat = input("Would you like to play again?")

if repeat == 0:
    print(story)

elif:
    print("Thank you for playing!")

else:
    print("Please enter a valid response.")
