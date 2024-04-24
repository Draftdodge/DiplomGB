from django.contrib import admin
from parkings import models
# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'parking_spot', 'parking', 'start_access_date', 'end_access_date', 'payment']
    fields = ['client', 'parking_spot', 'parking', 'end_access_date', 'payment']
    readonly_fields = ['payment']
    list_filter = ['start_access_date', 'payment']

admin.site.register(models.Order, OrderAdmin)