from django.shortcuts import render
from catalog.models import Author,BookInstance,Book,Language,Genre
from django.views import generic
from django.shortcuts import get_object_or_404


# Create index view for home page.
def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # How many books are available when (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    num_authors = Author.objects.count()


    context = {
        'num_books':num_books,
        'num_instances':num_instances,
        'num_instances_available':num_instances_available,
        'num_authors':num_authors
    }

    return render(request,'index.html',context=context)

class BookListView(generic.ListView):
    model = Book
    context_object_name = 'my_book_list'   # our specified name for he list as a template variable
    queryset = Book.objects.all()  # Fetch 2 books contianing title Django
    template_name = 'book_list.html'


class BookDetailView(generic.DetailView):
    model = Book


def book_detail_view(request, primary_key):
    book = get_object_or_404(Book,pk=primary_key)
    return render(request,'catalog/book_detail.html',context={'book':book})

