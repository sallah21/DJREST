from django import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import context, loader
from .models import Beer, Brewery

# Create your views here.
def index(request):
    beer_list = Beer.objects.all()
    template = loader.get_template('myapp/index.html')
    # output = ", ".join([q.name for q in beer_list])
    context = {'beer_list': beer_list,}
    return HttpResponse(template.render(context, request))


def id(request, Id):
    beer = Beer.objects.filter(id = Id).all()
    template = loader.get_template('myapp/beer.html')
    context = {'beer':beer,}
    return HttpResponse(template.render(context, request))

def name(request, name):
    beer_list = Beer.objects.filter(name = name).all()
    output = ", ".join([q.name for q in beer_list])
    return HttpResponse(output)


def brewery(request, brewery_name):
    beer_list = Brewery.objects.filter(name = brewery_name).all()
    output = ", ".join([q.name for q in beer_list])
    output2 = ", ".join([q.owner for q in beer_list])
    output3 = ", ".join([q.country for q in beer_list])
    output += ' '
    output += output2
    output += ' '
    output += output3
    return HttpResponse(output)


def  type(request, type_name):
    type_list = Beer.objects.filter(type = type_name).all()
    output = ", ".join([q.name for q in type_list])
    return HttpResponse(output)