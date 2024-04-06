from django.contrib import admin
from .models import Schedule, Record


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'coach', 'gym', 'start_time', 'end_time', 'weekday')
    list_filter = ('weekday', 'gym', 'coach')
    search_fields = ('gym__name', 'coach__user__first_name', 'coach__user__last_name')
    ordering = ('weekday', 'start_time')


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'coach_name', 'gym', 'start_time', 'end_time')
    list_filter = ('gym', 'coach', 'client')
    search_fields = ('gym', 'coach__user__first_name', 'coach__user__last_name', 'client__first_name', 'client__last_name')
    date_hierarchy = 'start_time'
    ordering = ('-start_time',)

    def client_name(self, obj):
        return obj.client.get_full_name()

    client_name.short_description = 'Client'

    def coach_name(self, obj):
        return obj.coach.user.get_full_name()

    coach_name.short_description = 'Coach'

