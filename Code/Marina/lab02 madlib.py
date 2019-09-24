import random

print("Hello, dear user, welcome to my mad Frost!\n")

place = input("Name several natural places separated by commas, no spaces: ")
precipitation = input("Name several kinds of precipitation separated by commas, no spaces: ")
farm_animal = input("Name several kinds of farm animals separated by commas, no spaces: ")
feeling = input("Name several kinds of feelings separated by commas, no spaces: ")
verb = input("Name several verbs separated by commas, no spaces: ")
adverb = input("Name several adverbsseparated by commas, no spaces: ")
water = input("Name several bodies of water separated by commas, no spaces: ")
time_of_day = input("Name several times of day separated by commas, no spaces: ")
noun = input("Name several nouns separated by commas, no spaces: ")
measure = input("Name several units of measuremen separated by commas, no spaces: ")

print("\n")
#
print("Thanks, here is your mad Frost lib!\n")

place_list = place.split(',')
prec_list = precipitation.split(',')
animal_list = farm_animal.split(',')
feeling_list = feeling.split(',')
verb_list = verb.split(',')
adverb_list = adverb.split(',')
water_list = water.split(',')
time_list = time_of_day.split(',')
noun_list = noun.split(',')
measure_list = measure.split(',')

place_random = random.choice(place_list)
prec_random = random.choice(prec_list)
animal_random = random.choice(animal_list)
feeling_random = random.choice(feeling_list)
verb_random = random.choice(verb_list)
adverb_random = random.choice(adverb_list)
water_random = random.choice(water_list)
time_random = random.choice(time_list)
noun_random = random.choice(noun_list)
measure_random = lambda: random.choice(measure_list)



print("\n")

print(f"Whose {place_random} this is I think I know.\nHis {noun_random} is in the village though;\nHe will not {feeling_random} me stopping here\nTo {verb_random} his {place_random} fill up with {prec_random}.\nMy little {animal_random} must think it {adverb_random}\nTo {verb_random} without a farmhouse near\nBetween the {place_random} and frozen {water_random}\nThe darkest {time_random} of the year.\nThe {place_random} are {adverb_random}, dark and deep,\nBut I have {noun_random} to keep,\nAnd {measure_random()} to go before I sleep,\nAnd {measure_random()} to go before I sleep.")
