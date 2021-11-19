from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
urlpatterns = [
    #path('<slug:name>', views.name, name='name'),
    path('brewery/<int:brewery_id>', views.brewery, name='Brewery name'),
    path('type/<slug:type_name>', views.type, name='Type name'),
    path('', views.index, name='index'),
    #path('', include(router.urls)),
    path('<int:Id>/', views.id, name='id'),
    path('add/', views.add, name='add'),
 path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('beers/', views.BeersViewSet, name='beers')
   

]
