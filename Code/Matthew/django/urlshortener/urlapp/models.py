from django.db import models
from urllib.parse import urlparse



class UrlShort(models.Model):
    user_url = models.CharField(max_length=500)
    code = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return 'http://.../' + self.code
    
    def url_domain(self):
        parsed_uri = urlparse(self.user_url)
        return parsed_uri.netloc
        




