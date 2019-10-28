from django.db import models

class Todoitem(models.Model):
    body = models.CharField(max_length=69)
    create_date = models.DateTimeField(auto_now_add = True)
    complete_date = models.DateTimeField(blank=True, null=True)
    completion_status = models.BooleanField()

    def __str__(self):
        return f'{self.body}: {self.completion_status}'

