from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birthday = models.DateField()
    pnone_number = models.CharField(max_length=12)
    is_cell = models.BooleanField()

    def __str__(self):
        return self.first_name + self.last_name
