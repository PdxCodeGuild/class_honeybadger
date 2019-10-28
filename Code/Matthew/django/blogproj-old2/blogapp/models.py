from django.db import models


class BlogPostType(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name + ' ' + str(self.posts.count()) + ' posts'


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    type = models.ForeignKey(BlogPostType, on_delete=models.SET_NULL, related_name='posts', null=True, blank=True)
    published_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title + ' ' + self.type.name
