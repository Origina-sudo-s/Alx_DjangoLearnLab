from django.contrib import admin
from .models import Book


# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = None
    form = None

    list_display = ('email', 'date_of_birth', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email, 'password)}),
        ('Personal info', {'fields': ('date_of_birth', 'profile_photo')}), 
        ('permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        ('important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'date_of_birth', 'profile_photo', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)

    admin.site.register(CustomUser, CustomUserAdmin)