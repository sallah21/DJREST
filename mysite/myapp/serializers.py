from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Beer, Brewery


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = User
        fields = ('url', 'username' , 'email' , 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Group
        fields = ('url', 'name')

class BeerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Beer
        fields = ('id', 'name', 'alc', 'ibu', 'type', 'brewery', 'description')