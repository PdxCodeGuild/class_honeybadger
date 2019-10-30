from django.db import models

# add TodoItem class

class ToDoPost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date_posted = models.DateTimeField(auto_now_add = True)
    slug = models.CharField(max_length=200)
    date_completed = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
        # + "-" + self.date_posted
