# Django Admin Configuration for Book Model

## 1. Registered Model
```python
# bookshelf/admin.py
from django.contrib import admin
from .models import Book

admin.site.register(Book)
```

## 2. Custom Admin Class
```python
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('publication_year', 'author')
    search_fields = ('title', 'author')
    ordering = ('title',)

admin.site.register(Book, BookAdmin)
```

## Expected Admin Features:
- **List View**: Shows title, author, and publication year.
- **Filters**: Filter books by year or author.
- **Search**: Search by title or author.
- **Ordering**: Books sorted alphabetically by title.