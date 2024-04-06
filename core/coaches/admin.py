from django.contrib import admin
from .models import Coach


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'date_of_birth', 'gender', 'display_gyms')
    list_filter = ('gender', 'gyms')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'gyms__name')
    filter_horizontal = ('gyms',)

    def first_name(self, obj):
        return obj.user.first_name

    first_name.short_description = 'First Name'

    def last_name(self, obj):
        return obj.user.last_name

    last_name.short_description = 'Last Name'

    def display_gyms(self, obj):
        return ", ".join([gym.name for gym in obj.gyms.all()])

    display_gyms.short_description = 'Gyms'
