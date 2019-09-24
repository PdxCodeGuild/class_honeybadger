#filename: lab08_change_maker.py

#modules
import math

pennies=int(input("How many pennies do you have?\n"))

dollars = math.floor(pennies/100)
dorem = pennies % 100

quarters=math.floor(dorem/25)
qrem=dorem%25

dimes=math.floor(qrem/10)
direm=qrem%10

nickels=math.floor(direm/5)
nrem=direm%5

print("# of dollars...",dollars)
print("# of quarters...",quarters)
print("# of dimes...",dimes)
print("# of nickels...",nickels)
print("# of leftover pennies...",nrem)
