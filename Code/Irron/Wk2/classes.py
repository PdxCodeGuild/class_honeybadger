'''
Class example 

'''
class Animal:
    def __init__(self, name, sound): #this is the initiializer 
        self.name = name   #this is a member variable
        self.sound = sound #this is a member variable
        
    def make_sound(self):
        return f'{self.name} says {self.sound}'

class Dog(Animal): # inherit from Animal
    def __init__(self, name, sound, number_of_legs):
        super().__init__(name, sound) # invoke the parent's initializer

class Cat(Animal): # inherit from Animal
    def __init__(self, name, sound, number_of_ears):
        super().__init__(name, sound) # invoke the parent's initializer
        self.number_of_ears = number_of_ears


dog1 = Dog('Clarence', 'woof', 4)
print(dog1.make_sound())

cat1 = Cat('Meowser', 'i really fucking hate all hoomans', 1)
print(cat1.make_sound())
print(cat1.number_of_ears)