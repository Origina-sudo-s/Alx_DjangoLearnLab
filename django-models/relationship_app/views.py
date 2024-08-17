# relationship_app/view.py
from django.shortcuts import render
from relationship_app.models import Book


# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})



from django.views.generic.detail import DetailView
from relationship_app.models import Library
from .models import Library 
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
# relationship_app/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .decorators import admin_required

@login_required
@admin_required
def admin_view(request):
    # Your view logic here
    return render(request, 'relationship_app/admin_view.html')


# relationship_app/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')

@user_passes_test(is_librarian)
def libraries_view(request):
    return render(request, 'librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html')