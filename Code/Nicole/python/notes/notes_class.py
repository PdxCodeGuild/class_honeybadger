# notes_class.py

# defining a class

class Name:
    def __init__(self, first, last):
        self.first = first
        self.last = last


    # creates a return string when calling the class in a print statement
    def __str__(self):
        return f"My name is {self.first} {self.last}."


me = Name("Nicole", "Young")
print(me)