from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.books, name='books'),
    path('create/<int:id>/create_comment/', views.create_comment, name='create_comment'),
    path('books/<int:id>/', views.get_book, name='book'),

    path('books/admin-books/', views.admin_books, name='admin_books'),
    path('books/new/', views.create_book, name='create_book'),
    path('books/update/<int:id>', views.update_book, name='update_book'),
    path('books/delete/<int:id>', views.delete_book, name='delete_book'),

    path('admin-authors/', views.admin_authors, name='admin_authors'),
    path('authors/new/', views.create_author, name='create_author'),
    path('authors/update/<int:id>', views.update_author, name='update_author'),
    path('authors/delete/<int:id>', views.delete_author, name='delete_author')
]

