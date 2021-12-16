from django.contrib import admin
from .models import ParkingSpace, ReservedPlace


class ReservedPlaceAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'parking_space', 'date_start_parking', 'date_finish_parking']
    list_display_links = ['user']


class ParkingSpaceAdmin(admin.ModelAdmin):
    list_display = ['parking_space_number']
    list_display_links = ['parking_space_number']


admin.site.register(ParkingSpace, ParkingSpaceAdmin)
admin.site.register(ReservedPlace, ReservedPlaceAdmin)
