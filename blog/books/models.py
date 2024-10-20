from django.db import models

# Create your models here.


#defining a data model for Author
class Author(models.Model):

    name=models.CharField(max_length=150)
    birth_date=models.IntegerField()

    def __str__(self):

        return self.name



class BookManager(models.Manager):


    def get_published_books(self):
        
        return self.filter(is_published=True)  


#defining a data model for Book

class Book(models.Model):

    title=models.CharField(max_length=200)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    publication_date=models.DateField()
    is_published=models.BooleanField(default=False)
    objects=BookManager()

    def __str__(self):
        return self.title
