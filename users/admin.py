from django.contrib import admin

from .models import SiteClient


@admin.register(SiteClient)
class SiteClientAdmin(admin.ModelAdmin):
    fields = ["username", "password", "email"]
