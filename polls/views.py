from django.shortcuts import render
from django.http import HttpResponse
from django_api_tutorial.settings import BASE_DIR, DATABASE_DIR


# Create your views here.

def index(request):
    return HttpResponse(
        'Hello, world. Here is the polls index. <br />The base_dir is ' +
        BASE_DIR + '<br />' + 'The database dir is ' + DATABASE_DIR)
