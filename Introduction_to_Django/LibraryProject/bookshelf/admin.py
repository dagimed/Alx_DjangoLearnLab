from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add filters by publication year and author
    list_filter = ('publication_year', 'author')
    
    # Enable search by title and author
    search_fields = ('title', 'author')
    
    # Optionally: Order books by title by default
    ordering = ('title',)

# Register with customizations
admin.site.register(Book, BookAdmin)