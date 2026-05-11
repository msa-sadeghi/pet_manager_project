from django.contrib import admin
from .models import Vaccine, VetVisit


@admin.register(Vaccine)
class VaccineAdmin(admin.ModelAdmin):
    list_display = ["pet", "name", "date_given", "next_due", "administered_by"]
    list_filter = ["name", "date_given"]
    search_fields = ["pet__name", "name"]


@admin.register(VetVisit)  
class VetVisitAdmin(admin.ModelAdmin):
    list_display = ['pet', 'visit_date', 'visit_type', 'vet_name', 'cost']
    list_filter = ['visit_type', 'visit_date']
    search_fields = ['pet__name', 'vet_name']