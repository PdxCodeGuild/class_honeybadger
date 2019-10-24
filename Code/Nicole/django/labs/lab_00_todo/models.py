from django.db import models


class ToDoItem(models.Model):
    description_text = models.CharField(max_length=100)
    created_date = models.DateTimeField("date created")
    completed_date = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField()

    def __str__(self):
        return self.description_text
