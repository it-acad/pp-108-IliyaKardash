from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from book.models import Book
from author.models import Author
from order.models import Order


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'first_name', 'last_name',
                    'is_staff', 'is_active', 'role')
    list_filter = ('is_staff', 'is_active', 'role')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {
         'fields': ('first_name', 'last_name', 'middle_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
        ('Important Dates', {
         'fields': ('last_login', 'updated_at')}),
        ('Additional Info', {'fields': ('role',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'middle_name', 'role', 'is_staff', 'is_active', 'is_superuser'),
        }),
    )

    filter_horizontal = ()


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_title', 'get_full_author_name',
                    'description', 'count')
    list_filter = ('id', 'name', 'authors__name', 'authors__surname')

    def get_full_author_name(self, obj):
        return ', '.join([f'{author.name} {author.surname} {author.patronymic}' for author in obj.authors.all()])
    get_full_author_name.short_description = 'Author'

    def get_title(self, obj):
        return obj.name
    get_title.short_description = 'Title'


admin.site.register(Book, BookAdmin)
