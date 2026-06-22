from django.shortcuts import render
from .forms import RegistrationForm, UserUpdateForm, OwnerUpdateForm


def register_view(request):
    form = RegistrationForm()
    return render(request, "accounts/register.html", {"form": form})
