from django.db import models

class Todoitem(models.Model):
    body = models.CharField(max_length=69)
    create_date = models.DateTimeField()
    complete_date = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField()

    def __str__(self):
        return f'{self.id}: {self.body}'

