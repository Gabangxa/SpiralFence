from django.contrib import admin
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'first_payment_date', 'renewal_type', 'auto_renew', 'auto_renew_date', 'custom_notes')
    list_filter = ('renewal_type', 'auto_renew')
    search_fields = ('name', 'custom_notes')
    date_hierarchy = 'start_date'

admin.site.register(Service, ServiceAdmin)
