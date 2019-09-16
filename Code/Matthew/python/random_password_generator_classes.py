
import string
import random


class RandomCharacterGenerator:
    def __init__(self, character_set):
        self.character_set = character_set
    
    def get_random_character(self):
        return random.choice(self.character_set)


character_generators = [
    RandomCharacterGenerator(string.ascii_lowercase),
    RandomCharacterGenerator(string.ascii_uppercase),
    RandomCharacterGenerator(string.digits),
    RandomCharacterGenerator(string.punctuation)
]

password = ''
for i in range(10):
    character_generator = random.choice(character_generators)
    password += character_generator.get_random_character()
print(password)
    














class RandomPasswordGenerator:
    def __init__(self, n_lower, n_upper, n_number, n_special):
        self.n_lower = n_lower
        self.n_upper = n_upper
        self.n_number = n_number
        self.n_special = n_special
    
    def generate_password(self):
        password = ''
        for i in range(self.n_lower):
            password += random.choice(string.ascii_lowercase)
        for i in range(self.n_upper):
            password += random.choice(string.ascii_uppercase)
        for i in range(self.n_number):
            password += random.choice(string.digits)
        for i in range(self.n_special):
            password += random.choice(string.punctuation)
        
        password = list(password)
        random.shuffle(password)
        return ''.join(password)
    
    def __str__(self):
        return 'RandomPasswordGenerator'


rpg = RandomPasswordGenerator(3, 3, 3, 3)
rpg2 = RandomPasswordGenerator(4, 4, 4, 4)
print(rpg.generate_password())
print(rpg2.generate_password())


