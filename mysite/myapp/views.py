from django import template
from django.http import response
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse , Http404
from django.template import context, loader
from rest_framework.decorators import permission_classes
from rest_framework.parsers import JSONParser
from .models import Beer, Brewery
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from myapp.serializers import UserSerializer, GroupSerializer, BeerSerializer
import json
from django.core.serializers import serialize
from rest_framework.views import APIView
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
        beer_list = Brewery.objects.filter(id = brewery_id).all().distinct()
    except Brewery.DoesNotExist:
        raise Http404('Beer does not exist')
    data = serialize("json", beer_list, fields = ('id','name','country', 'type', 'owner'))
    return JsonResponse(data, safe=False)

def  type(request, type_name):
    #type_list = Beer.objects.filter(type = type_name).all()
    type_list = get_object_or_404(Beer, type=type_name)
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
    return ht(request,'myapp/add_beer.html')



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


def BeersViewSet(requset): 
        data = Beer.objects.all().distinct()
        #serializer_class = BeerSerializer
        Brew = Brewery.objects.all().distinct()
        data_list = list(data)
        brewery_list = list (Brew)
        comb = data_list + brewery_list
        data2 = serialize("json",data,  fields = ( 'id','name', 'alc', 'ibu', 'type', 'brewery', 'description'))
        Brew2 = serialize("json", Brew, fields = ('name','country', 'type', 'owner'))

        #permission_classes = [permissions.IsAuthenticated]
        #parser_classes = [JSONParser]
        #def get(self, reqest, format=None):
        #    return Response(request.data)
        return JsonResponse(data2,safe=False)