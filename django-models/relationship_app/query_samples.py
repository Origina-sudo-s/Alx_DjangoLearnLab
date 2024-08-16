import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django-models.settings')
django.setup()

from relationship_app.models import Autho, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books =Book.objects.filter(author=author)
        return [book.title for book in books]
    except Author.DoesNotExist:
        return[]

# List all books in a library
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        return [book.title for book in books]
    except Library.DoesNotExist:
        return[]

# Retrieve the librarian for a library

def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        return librarian.name
    except (Library.DoesNotExist, librarian.DoesNotExist):
        return None

if __name__ == '__main__':
    print("Books by Author 'George Orwell':", books_by_author('George Orwell'))
    print("Books in Library 'Central Library':", books_in_library('Central Library'))
    print("Librarian for library 'Central Library':", librarian_for_library('Central Library')) 
