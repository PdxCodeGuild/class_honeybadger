import random
#first real lab
adj1=input("Give us an adjetive: ")
adj2=input("Give us another now, come on: ")
verb1=input("A verb now, an action: ")
verb2=input("Three more verbs, I know you've got this: ")
nl = "\n"
txt=verb2.split(", ")
print(txt)

print(f"{nl}The elder spoke to the child: Inside of you there are two wolves: {nl}one is {adj1}, and the other is {adj2}. {nl}The child asked: Which will {verb1}? {nl}The elder replied: The one you {random.choice(txt)}.")
