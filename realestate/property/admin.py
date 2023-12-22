from django.contrib import admin
from .models import Property, Unit, Tenant

admin.site.register(Property)
admin.site.register(Unit)
admin.site.register(Tenant)
