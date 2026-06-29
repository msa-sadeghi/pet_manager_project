from django.shortcuts import render, redirect
from .forms import RegistrationForm, UserUpdateForm, OwnerUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate


def register_view(request):
    if request.user.is_authenticated:
        return redirect("pets:pet_list")
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            
            user = form.save()
            login(request, user)
        else:
            print(form.errors)
    else:
        form = RegistrationForm()
    return render(request, "accounts/register.html", {"form": form})


def login_view(request):

    if request.user.is_authenticated:
        return redirect("pets:pet_list")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("pets:pet_list")
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})


def logout_view(request):
    if request.method == "POST":

        logout(request)

    return redirect("accounts:login")
