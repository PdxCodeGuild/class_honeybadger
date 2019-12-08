from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    favorited_users = models.ManyToManyField(User, related_name='favorited_blog_posts')

    def __str__(self):
        return self.title

# class SavedBlogPost(models.Model):
#     blog_post = models.ForeignKey(BlogPost)
#     user = models.ForeignKey(User)


# bp = BlogPost.objects.get(id=1)
# print(bp.favorited_users.all())
#
# user = User.objects.get(id=1)
# print(user.favorited_blog_posts.all())
