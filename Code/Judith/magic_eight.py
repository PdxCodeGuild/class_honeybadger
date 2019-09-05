#filename: magic_eight.py

#import the damn library, fool
import random

#list of responses
response_list=[
"you do you, bud.",
"yeah sure why not",
"bad idea homie",
"oh you dirty dog",
"idk lemme alone",
"don't let your dreams be dreams",
"no",
"why are you asking me? follow ur heart <3",
"obv",
"hell naw"]

#welcom msg
print("yo wussup")

#user prompt
question=input("ask me a question dawg: ")

print(f"you asked: ", question)

#the void speaketh
print(random.choice(response_list))

#try a loop
#define a counter variable
i=0
#set a condition for the loop
while i<=3:
    #tells the user the position of i
    print("i:"+ str(i))

    #second ask, for giggles
    questiontwo=input("anything else fampai? ")

    print(f"you asked: ", questiontwo)

    #the void speaketh 2 electric boogaloo
    print(random.choice(response_list))

    i+=1
