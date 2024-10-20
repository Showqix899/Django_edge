from django.shortcuts import render
from django.views.generic import ListView
from .models import Book
# Create your views here.



#to show all the books listed in the database
class ListOfBooks(ListView):
    model = Book
    context_object_name = 'books'
    template_name='list_of_books.html'



#to show all the books that are published

class ListOfPublishedBooks(ListView):
    model=Book
    context_object_name='books'
    template_name='published_books.html'


    #using custom book manager in model to fetch only the published books
    def get_queryset(self):
        return Book.objects.get_published_books()
    