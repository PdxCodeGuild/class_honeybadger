from django.db import models

class Contactitem(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    birthday = models.DateField()
    phone_num = models.CharField(max_length = 10)
    is_cell = models.BooleanField()

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.birthday}: {self.phone_num}'