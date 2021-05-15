from django.shortcuts import render, redirect
from .models import Book, Author
# Create your views here.


def books(request):
    context = {
        "all_books": Book.objects.all()
    }
    return render(request, 'add_book.html', context)


def add_book(request):
    if request.method == "POST":
        Book.objects.create(
            title=request.POST['title'],
            desc=request.POST['description']
        )
    return redirect('/')


def authors(request):
    return render(request, 'add_author.html')


def add_author(request):
    if request.method == "POST":
        Author.objects.create(
            first_name=request.POST['firstName'],
            last_name=request.POST['lastName'],
            notes=request.POST['notes'],
            books=request.POST['books']
        )
    return redirect('/authors')


def see_author(request, id):
    return render(request, 'see_author.html')


def see_book(request, id):
    context = {
        "book": Book.objects.get(id=id),
        "authors": Author.objects.exclude(books__id=id)
    }
    return render(request, 'see_book.html', context)


def add_author_to_book(request, id):
    if request.method == "POST":
        book = Book.objects.get(id=id)
        author = Author.objects.get(id=request.POST['authorSelect'])
        book.authors.add(author)
    return redirect(f'/books/{id}')
    # worked here last
