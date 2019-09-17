





class Honeybadger:
    def __init__(self, name, age, aggression_level='medium'):
        self.name = name
        self.age = age
        self.aggression_level = aggression_level
        self.number_of_feet = 4
        
    def get_aggression_level(self):
        if self.aggression_level == 'high':
            return 'highly'
        elif self.aggression_level == 'medium':
            return 'moderately'
        else:
            return 'mildly'
    
    def __str__(self):
        return f'{self.age} year-old {self.name.title()} is a {self.get_aggression_level()} aggressive honeybadger'

    

bob = Honeybadger('bob', 3)
print(bob)


# 
# for key in bob.__dict__:
#     print(key)
    
    
# bob.name = bob.name.title()

# agg_level = bob.get_aggression_level()


# print(bob.aggression_level)
# print(bob.number_of_feet)











