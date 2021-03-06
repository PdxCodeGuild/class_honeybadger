


from django.core.management.base import BaseCommand

from blogapp.models import BlogPost
from django.contrib.auth.models import User
import random

lorem_ipsum = '''
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer eget nulla quis tellus congue elementum id auctor ipsum. Sed ornare rutrum metus, ultrices laoreet felis mollis quis. Sed faucibus lacus eu cursus fermentum. Duis porttitor ipsum et odio tincidunt laoreet. Fusce suscipit sapien arcu, eu luctus dui tincidunt non. Etiam pellentesque, est ac tristique tempor, diam nisi congue arcu, ut posuere turpis sem bibendum eros. Quisque vulputate, dolor vel auctor ultrices, mi metus tempus ante, ac maximus ante ex vel lorem. Vivamus tortor mauris, vehicula id risus id, congue sagittis diam. Cras scelerisque ullamcorper tortor.</p>

<p>Sed porta eros sit amet ligula egestas rhoncus. In sed consequat felis. Aliquam tempor risus tortor, a pretium ex laoreet eu. Proin elit eros, placerat eget ipsum ac, auctor elementum nisi. Mauris mollis convallis purus, et tempus arcu mattis vel. Quisque et lacus a dui interdum dignissim. Sed urna erat, malesuada nec dignissim cursus, malesuada quis nulla. Maecenas libero enim, vulputate semper neque a, blandit laoreet augue. Sed luctus nibh quis semper egestas. Cras et dolor ex. Pellentesque at magna lacus. Vestibulum tristique aliquet orci et cursus. Donec interdum purus libero, ac pulvinar enim mattis at. Phasellus mi justo, eleifend ac odio vitae, maximus mattis lorem. Nam at diam eu lacus lobortis molestie. Integer metus justo, malesuada vitae rutrum id, ornare eget dolor.</p>

<p>Nunc ultrices risus orci, non convallis elit scelerisque et. Nam justo nunc, molestie id libero id, lacinia euismod ligula. Curabitur interdum odio nisl, id hendrerit orci faucibus eu. Etiam id ante quis arcu egestas vulputate ut at ligula. Curabitur blandit eros quis metus ultrices scelerisque. Nulla ultricies libero sed urna tincidunt, vitae rutrum ante gravida. Morbi pulvinar id sapien a elementum. Nam feugiat nec eros quis placerat. In a justo consequat, scelerisque quam ut, pellentesque lacus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec risus nulla, ultricies non consequat eu, pulvinar ut magna. Vivamus ac maximus sem. Aenean sed facilisis lacus, ut efficitur neque. Ut luctus, ante interdum porttitor tristique, tellus odio iaculis lectus, non tincidunt urna justo eu tellus. Nullam faucibus id est sit amet venenatis. Quisque dictum efficitur lacus sed aliquet.</p>

<p>Integer fermentum efficitur urna, id consectetur ligula auctor at. Pellentesque odio neque, lacinia sed vestibulum nec, dictum id urna. Duis sed varius libero, sed fermentum lacus. Vivamus scelerisque vel est vitae faucibus. Proin dolor ante, tempor ut sagittis vitae, egestas in lectus. Phasellus ut justo sit amet turpis lacinia consequat. Curabitur scelerisque, odio at luctus molestie, ligula ligula semper purus, id dictum libero nulla at ante. Phasellus consequat ipsum ligula, congue commodo libero viverra nec. Sed quis lacus et magna vehicula dapibus eu et velit. Nullam sollicitudin ante eu sodales egestas.</p>

<p>Nunc laoreet eleifend purus, eu pellentesque erat congue nec. Nunc semper vel nunc viverra efficitur. Fusce facilisis, lectus a elementum dignissim, arcu dolor pellentesque odio, at sollicitudin sapien lorem ut enim. Nam sem diam, euismod eget metus ac, tempor lobortis felis. Nunc mattis facilisis turpis, nec porta tortor pellentesque eu. Proin luctus elit risus, eleifend rhoncus justo fermentum id. In hac habitasse platea dictumst. Proin id odio volutpat, sodales dui convallis, malesuada est. Donec vitae enim consequat, tristique urna fermentum, molestie quam. Nunc nibh dolor, feugiat non finibus sagittis, fermentum vitae lorem. Duis a convallis turpis. Donec lacinia maximus pretium. Nunc sit amet imperdiet sem. Nulla gravida ligula mauris, eget lobortis tortor fermentum eget. Donec quis vulputate urna.</p>
'''

class Command(BaseCommand):

    def handle(self, *args, **options):
        BlogPost.objects.all().delete()
        for i in range(100):
            title = f'Blog Post {i}'
            body = lorem_ipsum
            blog_post = BlogPost(title=title, body=body)
            blog_post.save()
            
            if random.random() < 0.1:
                user = random.choice(User.objects.all())
                blog_post.favorited_users.add(user)
