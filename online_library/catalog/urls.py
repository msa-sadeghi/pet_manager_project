from django.urls import path, re_path

from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    # IMPORTANT: specific patterns BEFORE the generic <slug:slug>
    path('books/', views.book_list, name='book_list'),
    path('books/random/', views.random_book, name='random_book'),
    re_path(r'^books/year/(?P<year>[0-9]{4})/$',
            views.books_by_year, name='books_by_year'),
    path('books/<slug:slug>/', views.book_detail, name='book_detail'),
    path('books/<slug:slug>/add-copy/', views.book_add_copy,
         name='book_add_copy'),

    path('categories/<slug:slug>/', views.category_detail,
         name='category_detail'),
    path('authors/<slug:slug>/', views.author_detail, name='author_detail'),

    path('loans/lookup/<uuid:token>/', views.loan_lookup, name='loan_lookup'),
    path('api/books/', views.api_books, name='api_books'),
    path('debug/request/', views.request_info, name='request_info'),
]
