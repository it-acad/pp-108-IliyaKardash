from typing import Any
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db.models.query import QuerySet
from .models import CustomUser
from book.models import Book
from author.models import Author
from order.models import Order
from django.contrib.admin import SimpleListFilter, TabularInline


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


class AuthorNameField(SimpleListFilter):
    title = 'Author name'
    parameter_name = 'author_name'

    def lookups(self, request: Any, model_admin: Any):
        authors = set(Book.objects.filter(
            authors__name__isnull=False).values_list('authors__name', flat=True))
        return [(author, author) for author in authors]

    def queryset(self, request: Any, queryset: QuerySet[Any]):
        if self.value():
            return queryset.filter(authors__name=self.value())
        return queryset


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_title', 'get_authors',
                    'description', 'year_of_publication', 'date_of_issue')
    readonly_fields = ('name', 'year_of_publication')
    list_filter = ('name', AuthorNameField, 'year_of_publication')

    fieldsets = (
        ('Static data', {
            'fields': ('name', 'authors', 'year_of_publication'),
        }),
        ('Dynamic data', {
            'fields': ('date_of_issue', 'description', 'count'),
        }),
    )

    filter_horizontal = ('authors',)

    def get_authors(self, obj):
        return ', '.join([f'{author.name} {author.surname}' for author in obj.authors.all()])
    get_authors.short_description = 'Authors'

    def get_full_author_name(self, obj):
        return ', '.join([f'{author.name} {author.surname} {author.patronymic}' for author in obj.authors.all()])
    get_full_author_name.short_description = 'Author'

    def get_title(self, obj):
        return obj.name
    get_title.short_description = 'Title'


admin.site.register(Book, BookAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'patronymic')
    list_filter = ('name', 'surname')

    fieldsets = (
        ('Personal Details', {
            'fields': ('name', 'surname', 'patronymic'),
        }),
    )

    filter_horizontal = ('books',)

    def get_books(self, obj):
        return ', '.join([book.name for book in obj.books.all()])
    get_books.short_description = 'Books'


admin.site.register(Author, AuthorAdmin)
