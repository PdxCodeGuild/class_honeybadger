from django.db import models

# Create your models here.
from django.db import models



class Contact(models.Model):
    # id = models.IntegerField...
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birthday = models.DateField()
    phone_number = models.CharField(max_length=200)
    is_cell = models.BooleanField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name
