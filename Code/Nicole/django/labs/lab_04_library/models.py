from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.last_name + ", " + self.first_name


class Book(models.Model):
    title = models.CharField(max_length=200)
    publish_date = models.DateTimeField()
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    checked_out = models.BooleanField()
    
    def __str__(self):
        return self.title + ", by " + self.author

    