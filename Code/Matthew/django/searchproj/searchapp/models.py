from django.db import models

class SearchTerm(models.Model):
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text
