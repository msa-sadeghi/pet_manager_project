from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Pet


@login_required
def view_all_pets(request):
    all_pets = Pet.objects.all()
    context = {"pets": all_pets}
    return render(request, "pets/pets_info.html", context)
