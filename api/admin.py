from django.contrib import admin
from .models import User, TravelRecord, InfectionRecord, Location


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'infection_probability')


class TravelRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'location', 'user', 'arrived_at')


class InfectionRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'infected_at')


class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'infection_factor')


admin.site.register(User, UserAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(TravelRecord, TravelRecordAdmin)
admin.site.register(InfectionRecord, InfectionRecordAdmin)

# Register your models here.
