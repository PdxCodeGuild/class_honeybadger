from django.db import models


class urlShort(models.Model):
    url_long = models.CharField(max_length=500)
    url_code = models.CharField(max_length=20)

    def __str__(self):
        return "http://.../" + self.url_code