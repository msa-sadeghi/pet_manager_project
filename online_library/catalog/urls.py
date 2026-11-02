from django.urls import path
from .views import home, about, book_detail

app_name = "catalog"
urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("books/<slug:slug>/", book_detail, name="book_detail"),
]
