

class Animal:

    def __init__(self, name, sound):

        self.name = name

        self.sound = sound

​

    def make_sound(self):

        return self.sound

​

class Dog(Animal): # inherit from Animal

    def __init__(self, name, sound):

        super().__init__(name, sound) # invoke the parent's initializer

​

class Cat(Animal): # inherit from Animal

    def __init__(self, name, sound):

        super().__init__(name, sound) # invoke the parent's initializer

​

s = Dog('Clarence', 'woof')

print(s.name)

print(s.sound)

​

​

s = Cat('Meowser', 'i hate all humans.')

print(s.name)

print(s.sound)

