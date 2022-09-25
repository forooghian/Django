from dataclasses import field
import imp
from adv.models import Adv, Category
from rest_framework import serializers


class AdvSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Adv
        fields = ['id', 'title', 'phone', 'price', 'date_created']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
