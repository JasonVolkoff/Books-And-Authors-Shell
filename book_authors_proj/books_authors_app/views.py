from django.shortcuts import render, redirect
from .models import Book, Author
# Create your views here.


def books(request):  # path('', views.books),
    context = {
        "all_books": Book.objects.all()
    }
    return render(request, 'add_book.html', context)


def add_book(request):  # path('add_book', views.add_book),
    if request.method == "POST":
        Book.objects.create(
            title=request.POST['title'],
            desc=request.POST['description']
        )
    return redirect('/')


def authors(request):  # path('authors', views.authors),
    context = {
        "all_authors": Author.objects.all()
    }
    return render(request, 'add_author.html', context)


def add_author(request):  # path('add_author', views.add_author),
    if request.method == "POST":
        Author.objects.create(
            first_name=request.POST['firstName'],
            last_name=request.POST['lastName'],
            notes=request.POST['notes'],
        )
    return redirect('/authors')


def see_author(request, id):  # path('authors/<int:id>', views.see_author),
    context = {
        "books": Book.objects.exclude(authors__id=id),
        "author": Author.objects.get(id=id)
    }
    return render(request, 'see_author.html', context)


def see_book(request, id):  # path('books/<int:id>', views.see_book),
    context = {
        "book": Book.objects.get(id=id),
        "authors": Author.objects.exclude(books__id=id)
    }
    return render(request, 'see_book.html', context)


# path('authors/<int:id>/add_author_to_book', views.add_author_to_book),
def add_author_to_book(request, id):
    if request.method == "POST":
        book = Book.objects.get(id=id)
        author = Author.objects.get(id=request.POST['authorSelect'])
        book.authors.add(author)
    return redirect(f'/books/{id}')


# path('books/<int:id>/add_book_to_author', views.add_book_to_author),
def add_book_to_author(request, id):
    if request.method == "POST":
        author = Author.objects.get(id=id)
        book = Book.objects.get(id=request.POST['bookSelect'])
        author.books.add(book)
    return redirect(f'/authors/{id}')
