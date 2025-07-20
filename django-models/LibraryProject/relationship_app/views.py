# views.py
from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library 

# 1.1 Function-Based View
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# 1.2 Class-Based View
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
