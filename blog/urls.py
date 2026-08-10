from django.urls import path
from .views import post_list, post_detail, contact, post_create, post_update

app_name = "blog"
urlpatterns = [
    path("", post_list, name="post_list"),
    path("post_create", post_create, name="post_create"),
    path("post/<int:pk>/", post_detail, name="post_detail"),
    path("contact/", contact, name="contact"),
]
