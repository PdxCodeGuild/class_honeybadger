#filename: babbytalk_gen.py

#goal: randomly select three syllables to creat baby babbytalk
#ex: goo ga ma da ba

#step1: define a list of possible syllables: goo ga ma da ba
#step2: randomly choose three syllables and append to variable
#step3: print result

#modules
import random

#variables
syllables=["goo","ga","ma","da","ba"]
#define babbytalk outside of loop as a global variable so the whole program can access it
babbytalk=""

#user input for number of syllables
sylcount=input("How much babbytalk do you want? ")

for x in range(int(sylcount)):
    babbytalk+=(random.choice(syllables))
    #babbytalk=babbytalk+random.choice(syllables)
    #print("Loop"+str(x))
    print(babbytalk)

'''if....:
babbytalk='''
