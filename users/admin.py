from django.contrib import admin

from .models import SiteClient, Subscription


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    fields = ["name", "add_todolists", "add_tasks_by_list"]


@admin.register(SiteClient)
class SiteClientAdmin(admin.ModelAdmin):
    fields = ["username", "password", "email", "subscription"]
