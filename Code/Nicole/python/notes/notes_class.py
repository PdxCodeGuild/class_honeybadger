# notes_class.py

# defining a class

class Person:
    def __init__(self, full_name):
        name = full_name.split(" ")
        self.first_name = name[0]
        self.last_name = name[1]
    
    def child(self, p):
        full_name = self.first_name + "-Jr." + " " + self.last_name + "-" + p.last_name
        return Person(full_name)

    # creates a return string when calling the class in a print statement
    def __str__(self):
        return f"My name is {self.first_name} {self.last_name}."

p = Person("Nicole Young")
print(p.first_name)
print(p)
q = Person("Jim Slim")
print(p.child(q))