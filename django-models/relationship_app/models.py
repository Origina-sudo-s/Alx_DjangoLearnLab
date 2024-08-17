from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=CASCADE)

    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.ManyToManyField(Book, related_name='libraries')

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# relationship_app/models.py
from django.db import models
from django.contrib.auth.models import Admin

class AdminProfile(models.Model):

    Admin_role= (
    ('Admin', 'Admin'),
    ('Member', 'Member'),
    ('Admin'),
    ('Librarian', 'Librarian'),
    ('Member'),
    )
    Admin = models.OneToOneField(UserAdmin, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=Admin_role, default='Member')

    def __str__(self):
        return f'{self.user.username} - {self.role}'
        