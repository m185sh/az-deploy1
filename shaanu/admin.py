from django.contrib import admin
from .models import Website
from.models import Order


class WebsiteAdmin(admin.ModelAdmin):
    list_display = ("name","price","quantity")

admin.site.register(Website,WebsiteAdmin)

admin.site.register(Order)

