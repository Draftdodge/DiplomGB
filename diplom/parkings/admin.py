from django.contrib import admin
from . import models

@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(amount=0)

class ClientAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone', 'car_number', 'key_number', 'access', 'phone_access', 'key_access',
                    'start_access_date', 'end_access_date','description', 'added_at', 'parking', 'parking_spot']
    ordering = ['-full_name']
    list_filter = ['access', 'phone_access', 'key_access', 'parking']
    search_fields = ['phone', 'key_number']
    search_help_text = 'Поиск по полю "Телефон" и "Номер ключа"'
    actions = [reset_quantity]
    fields = ['full_name', 'phone', 'car_number', 'key_number', 'access', 'phone_access', 'key_access',
                    'end_access_date','description', 'added_at', 'parking', 'parking_spot']
    readonly_fields = ['added_at']

class ParkingAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'number_of_spot', 'phone', 'scheme', 'reg_date']
    ordering = ['name']
    search_fields = ['name']
    search_help_text = 'Поиск по имени (name)'
    readonly_fields = ['reg_date']

admin.site.register(models.Client, ClientAdmin)
admin.site.register(models.Parking, ParkingAdmin)

