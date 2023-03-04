from urllib import request
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def Index(request):
    return Response('Welcome to Divar Api HomePage')


@api_view(['GET'])
def Advertisements(request):
    return Response('Advertisements')


@api_view(['POST'])
def AddNewAdvertisement(request):
    return Response('AddNewAdvertisement')


@api_view(['PUT'])
def UpdateAdvertisement(request):
    return Response('UpdateAdvertisement')


@api_view(['POST'])
def RemoveAdvertisement(request):
    return Response('RemoveAdvertisement')
