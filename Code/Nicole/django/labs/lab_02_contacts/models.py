from django.db import models



class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField()
    phone_number = models.CharField(max_length=12)
    is_cell = models.BooleanField()
    
    def __str__(self):
        return self.last_name + ", " + self.first_name

