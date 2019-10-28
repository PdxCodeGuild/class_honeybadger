

from django.core.management.base import BaseCommand

from blogapp.models import BlogPost

class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('./blogapp/management/commands/lorem_ipsum.txt', 'r') as file:
            lorem_ipsum = file.read()
        for blog_post in BlogPost.objects.all():
            blog_post.body = lorem_ipsum
            blog_post.save()


