from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Book

# Define a custom admin class
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'date_of_birth', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

# Register the custom user and the Book model
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Book)
