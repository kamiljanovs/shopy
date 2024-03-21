from django.shortcuts import render
from django.http import HttpResponse
import datetime
from product.models import Product


def main_page_view(request):
    MOCK_DATA = [
        {
            'id': 1,
            'name': 'John',
            'age': 25
        },
        {
            'id': 2,
            'name': 'Jane',
            'age': 30
        },
        {
            'id': 3,
            'name': 'Bob',
            'age': 35
        }
    ]
    context = {'name': 'Adilet', 'mock_data': MOCK_DATA}
    if request.method == 'GET':
        return render(request, 'main.html', context=context)

def hello_view(request):
    return HttpResponse("Hello! Its my project")

def current_date_view(request):
    return HttpResponse('Current date is %s' % datetime.date.today())

def goodby_view(request):
    return HttpResponse("Goodby user!")

def product_list_view(request):
    products = Product.objects.all()
    # print(products)
    context = {'products': products}
    return render(request, 'product_list.html', context)
