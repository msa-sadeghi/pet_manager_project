from django.shortcuts import render
from .forms import RegistrationForm, UserUpdateForm, OwnerUpdateForm
from django.contrib.auth.forms import AuthenticationForm


def register_view(request):
    form = RegistrationForm()
    return render(request, "accounts/register.html", {"form": form})


def login_view(request):
    form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})
