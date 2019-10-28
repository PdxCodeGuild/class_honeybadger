from django.db import models


class BlogPostCategory(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class BlogPost(models.Model):
    # id = models.IntegerField...
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    body = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True) # updated when created
    date_edited = models.DateTimeField(auto_now=True) # updated when saved
    category = models.ForeignKey(BlogPostCategory, on_delete=models.PROTECT, related_name='posts')
    
    def html_body(self):
        return self.body.replace('\n', '<br/>')
    
    def __str__(self):
        return self.title + ' - ' + self.author

# blog_post = BlogPost.objects.get(id=1)
# blog_post.category.name
# 
# blog_post_category = BlogPostCategory.objects.get(id=1)
# blog_post_category.posts.all()
