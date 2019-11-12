from django.db import models

class VocabItem(models.Model):
    word = models.CharField(max_length=50)
    definition = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.word

