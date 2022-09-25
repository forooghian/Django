from rest_framework import viewsets
from rest_framework import permissions
from adv.models import Category, Adv
from .serializers import AdvSerializer, CategorySerializer


class AdvViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Adv.objects.all()
    serializer_class = AdvSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
