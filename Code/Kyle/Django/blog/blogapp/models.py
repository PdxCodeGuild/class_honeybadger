from django.db import models

class BlogPostType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    type = models.ForeignKey(BlogPostType, on_delete=models.PROTECT)
    date_created = models.DateTimeField()

    def pretty_date(self):
        return self.date_created.strftime('%B %d')

    def __str__(self):
        return self.title
