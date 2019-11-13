from django.db import models

# Create your models here.
class UrlCode(models.Model):
    url = models.CharField(max_length=500)
    code = models.CharField(max_length=20)
    def __str__(self):
        return self.url
