from django.contrib import admin
from .models import Book, Author, Category, Publisher

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'birth_date')
    search_fields = ('first_name', 'last_name')
    prepopulated_fields = {'slug':('first_name', 'last_name')}

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'website')
    search_fields = ('name', 'city')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug':('name',)}

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'category',
                     'published_year', 'available_copies', 'is_active')
    list_filter = ('language', 'category', 'is_active')
    prepopulated_fields = {'slug':('title',)}
    readonly_fields = ('created_at', 'updated_at')
    list_editable=('is_active',)
    filter_horizontal = ("authors",)
    list_per_page = 20

    fieldsets = (
        ('اطلاعات اصلی', {
            'fields' : ('title', 'slug', 'isbn', 'description')
        }),
       ( 'روابط',{
            'fields':('authors', 'publisher', 'category')
        })
    )

    actions = ['deactivate_books']

    @admin.action(description='غیرفعال کردن کتاب های انتخاب شده')
    def deactivate_books(self, request, queryset):
        updated = queryset.update(is_active=False)
        self.message_user(request, f'{updated} کتاب غیر فعال شد')