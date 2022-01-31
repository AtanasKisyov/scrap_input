from django.contrib import admin
from .models import ActiveMaterial, ScrapTable


@admin.register(ActiveMaterial)
class RegisterMaterial(admin.ModelAdmin):
    list_display = ('material_number', 'material_description', 'inserted_on')


@admin.register(ScrapTable)
class RegisterScrapTable(admin.ModelAdmin):
    list_display = ('material_number', 'quantity', 'inserted_on')
