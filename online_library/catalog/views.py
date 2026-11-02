from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Book


def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return HttpResponse(f"{book.title}")


def home(request):
    return HttpResponse("<h1>به کتابخانه ما خوش آمدید</h1>")


def about(request):
    return HttpResponse("<h1>درباره ما</h1>")
