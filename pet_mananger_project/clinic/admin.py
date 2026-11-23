from django.contrib import admin
from .models import Vaccine, VetVisit
from django.utils.html import format_html


@admin.register(Vaccine)
class VaccinAdmin(admin.ModelAdmin):
    list_display = ["name", "pet", "date_given", "next_due", "overdue_status", "day_until_due"]
    list_filter = ["name"]
    search_fields = ["name", "pet__name"]

    def overdue_status(self, obj):
        if obj.is_overdue():
            return format_html("<span>expired</span>")
        return format_html("<span>valid</span>")

    overdue_status.short_description = "status"

    def day_until_due(self, obj):
        days = obj.days_until_due()
        return format_html("<span>{}</span>", days)

    day_until_due.short_description = "until due"


@admin.register(VetVisit)
class VetVisitAdmin(admin.ModelAdmin):
    pass
