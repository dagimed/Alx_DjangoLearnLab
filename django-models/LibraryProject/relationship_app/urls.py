from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import add_book, edit_book, delete_book

from Introduction_to_Django.LibraryProject.bookshelf import admin
from .views import list_books
from . import views

urlpatterns = [
    # Function & class-based views from earlier
    path('admin/', admin.site.urls),
    path('', include('relationship_app.urls')),
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # Registration still uses custom view
    path('register/', views.register_view, name='register'),

    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
    
    path('book/add/', add_book, name='add_book'),
    path('book/<int:pk>/edit/', edit_book, name='edit_book'),
    path('book/<int:pk>/delete/', delete_book, name='delete_book'),

]
