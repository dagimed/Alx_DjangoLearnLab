import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query: All books by a specific author (e.g., "George Orwell")
author_name = "George Orwell"
try:
    author = Author.objects.get(name=author_name)
    books_by_author = author.books.all()
    print(f"Books by {author_name}:")
    for book in books_by_author:
        print(f"- {book.title}")
except Author.DoesNotExist:
    print(f"No author found with name '{author_name}'")

# Query: List all books in a library (e.g., "City Library")
library_name = "City Library"
try:
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()
    print(f"\nBooks in {library_name}:")
    for book in books_in_library:
        print(f"- {book.title}")
except Library.DoesNotExist:
    print(f"No library found with name '{library_name}'")

# Query: Retrieve the librarian for a library (e.g., "City Library")
try:
    library = Library.objects.get(name=library_name)
    librarian = library.librarian
    print(f"\nLibrarian of {library_name}: {librarian.name}")
except Library.DoesNotExist:
    print(f"No library found with name '{library_name}'")
except Librarian.DoesNotExist:
    print(f"No librarian assigned to '{library_name}'")
