from django.shortcuts import render
from .models import Book
from django.db.models import Q

def book_list(request):
    query = request.GET.get('q')
    books = Book.objects.all()
    
    if query:
        books = books.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(authors__name__icontains=query) |
            Q(authors__surname__icontains=query) |
            Q(authors__patronymic__icontains=query)
        ).distinct()
    
    return render(request, 'book/book_list.html', {'books': books, 'query': query})