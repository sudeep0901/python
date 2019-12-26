from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
import requests, json

from .forms import BookForm

def index(request):
    resp = requests.get('http://localhost:5000/books')
    # print(resp.status_code)
    # print(type(resp.json()))
    books_dict = resp.json()
    dct_array = books_dict["books"]
    # if resp.status_code != 200:
            # This means something went wrong.
            # raise ApiError('GET /books/ {}'.format(resp.status_code))
    i = 0
    for book_item in dct_array:
        # print(book_item)
        # print(type(book_item))
        print('{} {}'.format(book_item['isbn'], book_item['name']))
        # context = {}
        # return HttpResponse(template.render(context, request))
    
    template = loader.get_template('books/index.html')
    context = {
        'books': dct_array,
    }
    return HttpResponse(template.render(context, request))
    # return HttpResponse("Hello, world. You're at the Books index.")

def detail(request, isbn_id):
    resp = requests.get('http://localhost:5000/books/{}'.format(isbn_id))
    book_dict = resp.json()
    print(book_dict)
    # template = loader.get_template('books/detail.html')
    # context = {
    #     'book': book_dict,
    # }
    return render(request, 'books/detail.html', {'books': book_dict})

    # return HttpResponse("You're looking at books %s." % isbn_id)

class Book:
    def __init__(self, name, isbn, price):
        self.name = name
        self.price = price
        self.isbn = isbn


def results(request, isbn_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % isbn_id)


def create(request):
    # newBook = {"name": "", "isbn":"", "price":0 }
    # return render(request, 'books/create.html', {'books': newBook})
    newBook = {
        'name': 'summary',
        'isbn': 0,
        'price': 0
    }

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            # pass
            print(form.data['name'])
            newBook = {
                'name': form.data['name'],
                'isbn': int(form.data['isbn']),
                'price':form.data['price']
            }
            resp = requests.post('http://localhost:5000/books', data= json.dumps(newBook), headers={'Content-Type':'application/json'})
            print(resp.status_code)
            if (resp.status_code ==  201):
                return HttpResponseRedirect("/books") 

            print("form submitted")
              # does nothing, just trigger the validation
    else:
        form = BookForm    
    
    return render(request, 'books/create.html', {'form': form})



def delete(request, isbn_id):
    print("delete request received")
    
    return HttpResponseRedirect("/books") 


# def create(request):

#     if request.method == 'POST':
#         print("Form Submitted............")
#     # if request.method = 
#     print(request.POST.get('name', False) )
#     form = BookForm(request.POST)
#     # newBook = {"name": "", "isbn":"", "price":0 }
#     # return render(request, 'books/create.html', {'books': newBook})
#     print(request)
#     newBook = {
#         # 'name': summary,
#         # 'isbn': description,
#         # 'price': price 
#     }
    
#     # resp = requests.post('http://localhost:5000/books/', data= json.dumps(newBook), headers={'Content-Type':'application/json'})
#     # print(resp.status_code)
#     return HttpResponseRedirect("/books")