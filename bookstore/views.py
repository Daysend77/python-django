import datetime

from django.shortcuts import render
from bookstore.models import Book, Author, Comment
from bookstore.forms import BookForm, AuthorForm, CommentForm
from django.shortcuts import redirect
from django.core.paginator import Paginator


def books(request):
    book_list = Book.objects.all()
    paginator = Paginator(book_list, 4)
    page = request.GET.get('page')
    books = paginator.get_page(page)
    return render(request, "bookstore/books.html", {'books': books})


def get_book(request, id):
    book = Book.objects.get(pk=id)
    comments = Comment.objects.filter(book_id=id)
    previous_link = request.META.get('HTTP_REFERER')
    form = CommentForm()
    return render(request, "bookstore/book.html", {'book': book,
                                                    'previous_link': previous_link,
                                                    'comments': comments,
                                                    'form': form})


def create_comment(request, id):
    form = CommentForm(request.POST)
    new_form = form.save(commit=False)
    new_form.book_id = int(id)
    new_form.time = datetime.datetime.now()
    new_form.save()
    previous_link = request.META.get('HTTP_REFERER')
    return redirect(previous_link)


def admin_books(request):
    books = Book.objects.all()
    form = BookForm()
    return render(request, 'bookstore/admin_books.html', {'form': form,
                                                          'books': books})


def create_book(request):
    form = BookForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('admin_books')


def update_book(request, id):
    book = Book.objects.get(id=id)
    form = BookForm(request.POST or None, instance=book)

    if form.is_valid():
        form.save()
        return redirect('admin_books')

    return render(request, 'bookstore/update_book.html', {'form': form})


def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('admin_books')


def admin_authors(request):
    authors = Author.objects.all()
    form = AuthorForm()
    return render(request, 'bookstore/admin_authors.html', {'form': form,
                                                            'authors': authors})


def create_author(request):
    form = AuthorForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('admin_authors')


def update_author(request, id):
    author = Author.objects.get(id=id)
    form = AuthorForm(request.POST or None, instance=author)

    if form.is_valid():
        form.save()
        return redirect('admin_authors')

    return render(request, 'bookstore/update_author.html', {'form': form})


def delete_author(request, id):
    author = Author.objects.get(id=id)
    author.delete()
    return redirect('admin_authors')



