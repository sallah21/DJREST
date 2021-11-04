from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("YoMenik")
def name(request, name):
    return HttpResponse("Nazwa piwska %s" %name)
def brewery(request, brewery_name):
    return HttpResponse("Nazwa browaru %s" %brewery_name)
def  type(request, type_name):
    return HttpResponse("Nazwa typu piwska %s" %type_name)