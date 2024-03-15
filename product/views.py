from django.shortcuts import render
from django.http import HttpResponse
import datetime

def hello_view(request):
    return HttpResponse("Hello! Its my project")

def current_date_view(request):
    return HttpResponse('Current date is %s' % datetime.date.today())

def goodby_viev(request):
    return HttpResponse("Goodby user!")

