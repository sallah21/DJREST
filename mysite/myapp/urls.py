from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('<slug:name>', views.name, name='name'),
    path('brewery/<int:brewery_id>', views.brewery, name='Brewery name'),
    path('type/<slug:type_name>', views.type, name='Type name'),
    path('', views.index, name='index'),
    path('<int:Id>/', views.id, name='id'),
    path('add/', views.add, name='add')
]
