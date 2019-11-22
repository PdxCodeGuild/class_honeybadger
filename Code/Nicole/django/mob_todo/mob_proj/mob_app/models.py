from django.db import models


class TodoList(models.Model):
    name = models.CharField(max_length=200)
    icon = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class TodoItem(models.Model):
    text = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(blank=True, null=True)
    list = models.ForeignKey(TodoList, on_delete=models.CASCADE, related_name="items")
    urgent = models.BooleanField()
    my_image = models.ImageField(upload_to='images/', null=True, blank=True)
    
    def __str__(self):
        return self.text