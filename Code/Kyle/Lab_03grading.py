#filename: Grading

print("Welcome to Grading App")

number = input("Enter Grade Percentage:")

if number.isdigit():
    number = int(number)

else:
    quit()

if number >= 0 and number <= 59:
    print("F")
elif number >= 60 and number <= 69:
    print("D")
elif number >= 70 and number <= 79:
    print("C")
elif number >= 80 and number <= 89:
    print("B")
elif number >= 90 and number <= 100:
    print("A")

else:
    print("you're number is outside  range")
