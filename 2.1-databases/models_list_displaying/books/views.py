from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    context = {}
    return render(request, template, context)

CONTENT = Book.objects.all()

def books_date(request, date):

    page_number = 1
    books_dates = [str(n.pub_date) for n in CONTENT]
    content = [n for n in CONTENT]
    if str(date) in books_dates:
        page_number = books_dates.index(str(date))
    paginator = Paginator(content, 1)
    page = paginator.get_page(page_number)
    template = 'books/book_date.html'
    book = Book.objects.get(pub_date=date)
    context = {"book_info": book, "date": date, 'page': page, 'book_date_list': books_dates}
    return render(request, template, context)




