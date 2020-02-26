from django.contrib import admin

# Register your models here.
from .models import Author,Genre,Book,Language,BookInstance

admin.site.register(Genre)

admin.site.register(Language)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name','first_name','date_of_birth','date_of_death')

# Registering the admin class for the Book using decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author')


# Registering the admin class for the BookInstance using decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status','due_back')

    fieldsets = (
        (None, {'fields':('book','imprint','id')}),
        ('Availability',{'fields':('status','due_back')})
    )





# admin.site.register(Author)
# admin.site.register(Book)
# admin.site.register(BookInstance)