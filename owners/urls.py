from django.urls import path
from .views import owner_detail

app_name = "owners"
urlpatterns = [path("<int:pk>/", owner_detail, name="owner_detail")]
