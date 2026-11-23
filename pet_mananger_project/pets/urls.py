from django.urls import path
from .views import view_all_pets

app_name = "pets"
urlpatterns = [path("", view_all_pets, name="pet_list")]
