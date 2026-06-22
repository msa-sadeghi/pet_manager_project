from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm
from owners.models import Owner


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=100, label="name", widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "name"})
    )
    last_name = forms.CharField(
        max_length=100,
        label="last_name",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "last name"}),
    )
    email = forms.CharField(
        max_length=100, label="email", widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "email"})
    )
    phone = forms.CharField(
        max_length=15, label="phone", widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "09xxxx"})
    )
    city = forms.CharField(
        max_length=100,
        required=False,
        label="city",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "city"}),
    )

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]


class UserUpdateForm(forms.ModelForm):
    class Meta:
        models = User
        fields = ["first_name", "last_name", "email"]


class OwnerUpdateForm(forms.ModelForm):
    class Meta:
        models = Owner
        fields = ["phone", "city", "address"]
