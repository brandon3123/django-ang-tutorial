from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from  .models import Book

# Create your views here.


class BookView(View):

    # gets all objects of a certain class
    books = Book.objects.all()
    # filter objects by a condition
    publishedBooks = Book.objects.filter(is_published=True)
    # fetch specified book
    firstBook = Book.objects.get(id=1)

    output = f"<h3> We have {len(books)} books in total </h3>"

    def get(self, request):
        return HttpResponse(self.output + self.display_titles())

    def display_titles(self):
        titles = "<ul>"
        for book in self.publishedBooks:
            titles += "<li>" + book.title + "</li>"

        titles += "</ul>"

        return titles

# method to return a view/response
def first(request):
    return HttpResponse("Hello World!")


def first_template(request):
    books = Book.objects.all()

    return render(request, "first_template.html", {"books": books})

