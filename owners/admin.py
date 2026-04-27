from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Owner


class OwnerInline(admin.StackedInline):
    model = Owner
    can_delete = True
    extra = 0


class CustomUserAdmin(UserAdmin):
    inlines = [OwnerInline]


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ["get_full_name", "phone", "city", "get_count"]

    def get_full_name(self, sample):
        return sample.user.get_full_name()

    get_full_name.short_description = "نام صاحب"

    def get_count(self, sample):
        return sample.pets.count()

    get_count.short_description = "تعداد حیوان"
