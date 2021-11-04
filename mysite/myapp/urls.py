from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('<int:name>', views.name, name='name'),
    path('<int:brewery_name>/Brewery', views.brewery, name='Brewery name'),
    path('<int:type_name>/Type', views.type, name='Type name'),
    path('', views.index, name='index')
]
