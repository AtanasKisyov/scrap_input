from django.contrib import admin
from .models import Material, ScrapTable


@admin.register(Material)
class RegisterMaterial(admin.ModelAdmin):
    list_display = ('material_number', 'material_description')


@admin.register(ScrapTable)
class RegisterScrapTable(admin.ModelAdmin):
    list_display = ('material_number', 'quantity')

