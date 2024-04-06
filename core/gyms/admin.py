from django.contrib import admin
from .models import Gym


@admin.register(Gym)
class GymAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'contact_number', 'email')
    search_fields = ('name', 'address', 'contact_number', 'email')
    list_filter = ('name',)