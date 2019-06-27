from django.contrib import admin
from catalog.models import Author, Genre, Book, BookInstance, Language

# Register your models here.

# admin.site.register(Author)
# admin.site.register(Book)
# admin.site.register(BookInstance)

admin.site.register(Genre)
admin.site.register(Language)

class BooksInline(admin.StackedInline):
	model = Book
	extra = 0

class AuthorAdmin(admin.ModelAdmin):
	list_display = (
		'last_name',
		'first_name',
		'date_of_birth',
		'date_of_death',
	)
	fields =['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
	inlines = [BooksInline]

admin.site.register(Author, AuthorAdmin)

class BooksInstanceInline(admin.TabularInline):
	model = BookInstance
	extra = 0

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'display_genre')
	list_filter = ('author', 'genre')
	inlines = [BooksInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
	list_display = (
		'book',
		'status',
		'borrower',
		'due_back',
		'language',
		'id',

	)
	list_filter = ('status', 'due_back')

	fieldsets = (
		(None, {
				'fields': ('book', 'imprint', 'id')
			}),
		('Availability', {
				'fields': ('status', 'due_back', 'borrower')
			})
	)	