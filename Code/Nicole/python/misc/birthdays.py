# birthdays.py

# 

from datetime import datetime
from datetime import date
from datetime import time

today = date.today()
print(today.strftime("%A, %B %d, %Y"))

# user_date = datetime.date(1979, 10, 1)
# print(user_date.strftime("%A, %B %d, %Y"))



exit()

class Person:
    def __init__(self, name, date):
        self.name = name
        self.date = date
    
    def current_age(self):
        birthday = self.date
        birthday
        return birthday
    
    def next_age(self):
        pass
    
    def __str__(self):
        return f"{self.name}'s birthday is on {self.date} and is currently {self.current_age()}"

# me = Person("Nicole", (1979, 10, 01))
# print(me)