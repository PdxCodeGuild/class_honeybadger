
from django.core.management.base import BaseCommand

from searchapp.models import SearchTerm

class Command(BaseCommand):

    def handle(self, *args, **options):
        SearchTerm.objects.all().delete()
        with open ('./searchapp/management/commands/english.txt', 'r') as file:
            words = file.read().split('\n')
        n = 0
        for word in words:
            if n%100 == 0:
                search_term = SearchTerm(text=word)
                search_term.save()
                print(n/len(words))
            n += 1
