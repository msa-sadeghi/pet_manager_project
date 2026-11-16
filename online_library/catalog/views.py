from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import (
    require_GET, require_http_methods, require_POST,
)

from .models import Author, Book, Category


def home(request):
    context = {
        'latest_books': Book.available.order_by('-created_at')[:6],
        'book_count': Book.objects.count(),
        'author_count': Author.objects.count(),
        'category_count': Category.objects.count(),
    }
    return render(request, 'catalog/home.html', context)


def about(request):
    return render(request, 'catalog/about.html')


def book_list(request):
    books = Book.objects.filter(is_active=True)

    q = request.GET.get('q', '').strip()
    if q:
        books = books.filter(title__icontains=q)

    lang = request.GET.get('lang', '')
    if lang in Book.Language.values:
        books = books.filter(language=lang)

    context = {
        'books': books,
        'q': q,
        'current_lang': lang,
        'languages': Book.Language.choices,
    }
    return render(request, 'catalog/book_list.html', context)


def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug, is_active=True)
    return render(request, 'catalog/book_detail.html', {'book': book})


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    books = category.books.filter(is_active=True)
    return render(request, 'catalog/category_detail.html',
                  {'category': category, 'books': books})


def author_detail(request, slug):
    author = get_object_or_404(Author, slug=slug)
    return render(request, 'catalog/author_detail.html',
                  {'author': author, 'books': author.books.filter(is_active=True)})


def books_by_year(request, year):
    year = int(year)                 # re_path groups are always strings
    books = Book.objects.filter(published_year=year, is_active=True)
    return render(request, 'catalog/book_list.html',
                  {'books': books, 'q': '', 'current_lang': '',
                   'languages': Book.Language.choices,
                   'page_title': f'کتاب‌های سال {year}'})


def loan_lookup(request, token):
    # token is already a uuid.UUID object thanks to <uuid:token>
    return HttpResponse(f'token = {token} (type: {type(token).__name__})')

def random_book(request):
    # token is already a uuid.UUID object thanks to <uuid:token>
    return HttpResponse(f'token')

def book_add_copy(request):
    # token is already a uuid.UUID object thanks to <uuid:token>
    return HttpResponse(f'token')
def api_books(request):
    # token is already a uuid.UUID object thanks to <uuid:token>
    return HttpResponse(f'token')
def request_info(request):
    # token is already a uuid.UUID object thanks to <uuid:token>
    return HttpResponse(f'token')
