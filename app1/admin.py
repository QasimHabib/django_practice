from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import  CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = (
        'username','password','email', 'first_name', 'last_name', 'is_staff','phone', 'gender',
        'address', 'province', 'city','district'
        )
    # fieldsets = (
    #     (None, {
    #         'fields': ('username', 'password1','password2', 'email', 'first_name', 'last_name', 'is_staff', 'phone', 'gender',
    #                    'address', 'province', 'city', 'district')
    #     }),
    # )
    add_fieldsets = (
        (None, {
            'fields': ('username','password1','password2', 'email', 'first_name', 'last_name', 'is_staff','phone', 'gender',
            'address', 'province', 'city', 'district')
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)