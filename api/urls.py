from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'api'


router = routers.DefaultRouter()
router.register(r'advs', views.AdvViewSet)
router.register(r'categories', views.CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
