from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book

# Create your views here.
@permission_required('app_name.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

@permission_required('app_name.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(book, pk=pk)
    if request.method == 'POST':
        #Process from submission
        pass
    return render(request, 'edit_book.html', {'books': books})


from django import forms
from.forms import ExampleForm

def example_view(request):
    form = ExampleForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'bookshelf/form_example.html', {'form': form})


class BookSearchForm(forms.Form):
    title = forms.CharField(max_length=100)
