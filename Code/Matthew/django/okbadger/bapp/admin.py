from django.contrib import admin

from .models import Gender, Orientation, Location, DatingProfile

admin.site.register(Gender)
admin.site.register(Orientation)
admin.site.register(Location)
admin.site.register(DatingProfile)
