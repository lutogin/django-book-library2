from django.contrib import admin
from catalog.models import Author, Genre, Book, BookInstance

# admin.site.register(Author)
# admin.site.register(Genre)
# admin.site.register(Book)
# admin.site.register(BookInstance)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death') # список полей для отобраения в админке
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')] # распределение полей при создании/редактировании модели


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


class BooksInstanceInline(admin.TabularInline):
    """
    Встроенное редактирование связанных записей.
    Объявив inlines, и указав тип TabularInline (горизонтальное расположение) или
    StackedInline (вертикальное расположение, так же как и в модели по умолчанию)
    """
    model = BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre') # список полей для отобраения в админке
    inlines = [BooksInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back') # список фильтров
    list_display = ('book', 'status', 'due_back') # список полей для отобраения в админке
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )
    """Набор полей при создании/редактировании модели"""
