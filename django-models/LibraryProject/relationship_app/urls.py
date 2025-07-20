from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books
from . import views

urlpatterns = [
    # Function & class-based views from earlier
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # Registration still uses custom view
    path('register/', views.register_view, name='register'),
]
