from django.contrib import admin

from services.models import Service, Subscription, Plan

admin.site.register(Service)
admin.site.register(Subscription)
admin.site.register(Plan)
