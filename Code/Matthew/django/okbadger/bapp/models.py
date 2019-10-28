from django.db import models

class Gender(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Orientation(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class DatingProfile(models.Model):
    name = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    occupation = models.CharField(max_length=200)
    age = models.IntegerField()
    bio = models.TextField()
    orientations = models.ManyToManyField(Orientation, blank=True)
    genders = models.ManyToManyField(Gender, blank=True)
    picture = models.ImageField(upload_to='profile_pics/', null=True)

    def __str__(self):
        return self.name
    
