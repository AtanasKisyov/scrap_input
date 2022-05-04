from django.contrib import admin

from scrap_input.scrap_app.models import Production, Area


@admin.register(Production)
class RegisterProduction(admin.ModelAdmin):
    pass


@admin.register(Area)
class RegisterArea(admin.ModelAdmin):
    pass
