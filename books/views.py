from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book

# Create your views here.
def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append("please enter a search term")
        elif len(q) > 20:
            errors.append("Please enter at most 20 characters")
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'books/search_result.html', {'books':books, 'query': q})
    return render(request, 'books/search_form.html', {'errors': errors})
        