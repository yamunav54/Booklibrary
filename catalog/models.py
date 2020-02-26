from django.db import models
from django.urls import reverse
import uuid

class Genre(models.Model):
    name = models.CharField(max_length=200,help_text='Enter book genre')

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=200, help_text='Enter Language')

    def __str__(self):
        return self.name

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=170)

    # foreignkey denotes that book has only one author but authors can have multiple books
    author = models.ForeignKey('Author',null=True,on_delete=models.SET_NULL)

    summary = models.TextField(max_length=1500,help_text='Enter book description')
    imprint = models.CharField(max_length=170)

    isbn = models.CharField('ISBN',max_length=13,help_text='Enter 13 Characters ISBN')

    # 1 Genre can belong to multiple books , books can cover multiple genres - Many - to - many relation

    genre =models.ManyToManyField(Genre,help_text='Choose genre for this book')
    languages = models.ManyToManyField(Language,help_text='Choose genre for this book')

    def __str__(self):
        # returning string for representing the Model Object
        return self.title

    def get_absolute_url(self):
        # return the exact url /books/id
        return reverse('book-detail',args=[str(self.id)])





class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True,blank=True)
    date_of_death = models.DateField('dead',null=True,blank=True)

    class Meta:
        ordering = ['last_name','first_name']

    def __str__(self):
        # returning string for representing the Model Object
        return f'{self.first_name}, {self.last_name}'

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,help_text='Book\'s unique Id')
    book = models.ForeignKey('Book',on_delete=models.SET_NULL,null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True,blank=True)


    LOAN_STATUS = (
        ('m','Maintenance'),
        ('o','On loan'),
        ('a','Availanble'),
        ('r','Reserved')
    )

    status = models.CharField(max_length=1,choices=LOAN_STATUS,blank=True,default='m',help_text='Book Availability')

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.id} {self.book.title}'




