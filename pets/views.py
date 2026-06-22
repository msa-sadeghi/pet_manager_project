from django.shortcuts import render
from .models import Pet
def view_all_pets(request):
    all_pets = Pet.objects.all()
    context = {
        'pets' : all_pets
    }
    return render(request, 'pets/pets_info.html', context)
