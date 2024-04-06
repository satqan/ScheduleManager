from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['id', 'username', 'full_name', 'role', 'is_staff']
    list_filter = ('is_staff', 'is_active', 'role')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)

    def full_name(self, obj):
        return obj.get_full_name()
    full_name.short_description = 'Full Name'





