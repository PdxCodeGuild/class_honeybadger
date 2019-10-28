from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Gender, Orientation, Location, DatingProfile

def index(request):
    dating_profiles = DatingProfile.objects.order_by('name')
    context = {
        'dating_profiles': dating_profiles
    }
    return render(request, 'bapp/index.html', context)

def profile(request, profile_id):
    context = {
        'dating_profile': DatingProfile.objects.get(id=profile_id)
    }
    return render(request, 'bapp/profile.html', context)


def create(request):
    context = {
        'locations': Location.objects.order_by('name'),
        'orientations': Orientation.objects.order_by('name'),
        'genders': Gender.objects.order_by('name')
    }
    return render(request, 'bapp/create.html', context)


def save_profile(request):
    d = request.POST
    profile_name = d['profile_name']
    profile_location_id = d['profile_location_id']
    profile_occupation = d['profile_occupation']
    profile_age = d['profile_age']
    profile_bio = d['profile_bio']
    profile_orientations = d.getlist('profile_orientations')
    profile_genders = d.getlist('profile_genders')
    profile_picture = request.FILES['profile_picture']
    
    # print(profile_name)
    # print(profile_location_id)
    # print(profile_occupation)
    # print(profile_age)
    # print(profile_bio)
    # print(profile_orientations)
    # print(profile_genders)
    # print(profile_picture)
    
    profile = DatingProfile(name=profile_name,
                            location_id=profile_location_id,
                            occupation=profile_occupation,
                            age=profile_age,
                            bio=profile_bio,
                            picture=profile_picture)
    profile.save()
    for orientation_id in profile_orientations:
        profile.orientations.add(Orientation.objects.get(id=orientation_id))
    for gender_id in profile_genders:
        profile.genders.add(Gender.objects.get(id=gender_id))
    
    # return HttpResponseRedirect(reverse('bapp:index'))
    return HttpResponseRedirect(reverse('bapp:profile', args=(profile.id,)))