from django.db import models
from django.urls import reverse
import uuid

# Create your models here.

class Language(models.Model):
	name = models.CharField(max_length=15, help_text='Book language')

	def __str__(self):
		return self.name

class Genre(models.Model):
	name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']

class Book(models.Model):
	title = models.CharField(max_length=200)
	author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
	isbn = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
	genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('book-detail', args=[str(self.id)])

	class Meta:
		ordering = ['title']

	def display_genre(self):
		return ', '.join(genre.name for genre in self.genre.all()[:3])

	display_genre.short_description = 'Genre'

class BookInstance(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
	book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
	language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
	imprint = models.CharField(max_length=200)
	due_back = models.DateField(null=True, blank=True)

	LOAN_STATUS = (
		('m', 'Maintenance'),
		('o', 'On loan'),
		('a', 'Available'),
		('r', 'Reserved'),
	)

	status = models.CharField(
		max_length=1,
		choices=LOAN_STATUS,
		blank=True,
		default='m',
		help_text='Book availability',
	)

	class Meta:
		ordering = ['book', 'status', 'due_back']

	def __str__(self):
		return '{0} ({1}) ({2})'.format(self.id, self.book.title, self.language.name)
	'''
	def __str__(self):
		if (self.due_back):
			return '{0} ({1}), Status: {2}, Due back: {3}'.format(
				self.book.title,
				self.language.name,
				self.get_status_display(),
				self.due_back.strftime('%d %B %Y'),
			)
		else:
			return '{0} ({1}), Status: {2}'.format(
				self.book.title,
				self.language.name,
				self.get_status_display()
			)
		'''

class Author(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	date_of_birth = models.DateField(null=True, blank=True)
	date_of_death = models.DateField('Died', null=True, blank=True)

	class Meta:
		ordering = ['last_name', 'first_name']

	def get_absolute_url(self):
		return reverse('author-detail', args=[str(self.id)])

	def __str__(self):
		return '{0}, {1}'.format(self.last_name, self.first_name)
