#filename: lab04_magic_eight.py

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

flag = True

while flag:
    #user prompt
    question=input("ask me a question friendo: ")

    print(f"you asked: ", question)

    #the void speaketh
    print(random.choice(response_list))

    if input('anything else fampai? ') in ['no','n','nah']:
        flag = False
