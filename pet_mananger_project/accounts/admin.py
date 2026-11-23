from django.contrib import admin
from .models import Profile, CustomUser
from django.contrib.auth.admin import UserAdmin

admin.site.register(Profile)


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name", "is_staff", "date_joined")
    list_filter = ("is_staff", "is_superuser", "is_active")
    search_fields = ("username", "email", "first_name", "last_name", "phone")

    fieldsets = UserAdmin.fieldsets + (
        (
            "اطلاعات اضافه",
            {
                "fields": ("bio", "avatar", "website", "phone", "birth_date"),
            },
        ),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (("اطلاعات اضافه", {"fields": ("email", "bio", "phone")}),)
