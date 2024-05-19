from django.contrib import admin
from ramailo.models import Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['idx', 'name']
    search_fields = ['idx', 'name']