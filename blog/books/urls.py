from django.urls import path
from .views import ListOfBooks,ListOfPublishedBooks

urlpatterns = [
    path('list/',ListOfBooks.as_view(),name='list'),
    path('published_books/',ListOfPublishedBooks.as_view(),name='published_list'),
]
