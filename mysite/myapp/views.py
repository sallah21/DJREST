from django import template
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse , Http404
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
    try:
        beer = Beer.objects.filter(id = Id).all()
    except Beer.DoesNotExist:
        raise Http404('Beer does not exist')
    #template = loader.get_template('myapp/beer.html')
    context = {'beer':beer,}
    return render(request,'myapp/beer.html', context)

def name(request, name):
    #beer_list = Beer.objects.filter(name = name).all()
    beer_list = get_object_or_404(Beer , name =name)
    output = ", ".join([q.name for q in beer_list])
    return HttpResponse(output)


def brewery(request, brewery_id):
    try:
        beer_list = Brewery.objects.filter(id = brewery_id).all().first
    except Brewery.DoesNotExist:
        raise Http404('Beer does not exist')

    #output = ", ".join([q.name for q in beer_list])
    #output2 = ", ".join([q.owner for q in beer_list])
    #output3 = ", ".join([q.country for q in beer_list])
    #output += ' '
    #output += output2
    #output += ' '
    #output += output3
    context = {'brewery':beer_list}
    return HttpResponse(render(request, 'myapp/brewery.html',context))

def  type(request, type_name):
    #type_list = Beer.objects.filter(type = type_name).all()
    type_list = get_object_or_404(Beer, type=type_name)

    #output = ", ".join([q.name for q in type_list])
    context ={'type':type_list,'type_name':type_name
    }
    return render(request,'myapp/brewery.html', context)


def add(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('alc') and request.POST.get('ibu') and request.POST.get('type') and request.POST.get('brewery'):
            beer = Beer()
            beer.name = request.POST.get('name')
            beer.alc = request.POST.get('alc')
            beer.ibu = request.POST.get('ibu')
            beer.type = request.POST.get('type')
            nm = request.POST.get('name')
            brewid =get_object_or_404(Brewery, name =request.POST.get('brewery') )
            beer.brewery = brewid
            beer.description = request.POST.get('description')
            beer.save()
    return render(request,'myapp/add_beer.html')
