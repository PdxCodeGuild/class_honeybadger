import random

# greeting
print("*" *10)
print("\nWelcome to the zoo! I'll be your guide for today.\n")

# define the list
animals = input("Please type three animals you want to see today, separated by commas: ").split(",")

animal1 = random.choice(animals)

print(f"The first animal we will see on the tour is the {animal1},\n")

animals.remove(animal1)
animal2 = random.choice(animals)

print(f"The second animal we will see is the {animal2},\n")

animals.remove(animal2)
animal3 = random.choice(animals)

print(f"The last animal we will see on the tour is the {animal3},\n")

animals.remove(animal3)
