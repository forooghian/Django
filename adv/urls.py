from django.urls import path
from . import views

app_name = 'adv'


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:adv_id>', views.detail, name='detail')
]
