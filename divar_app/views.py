from urllib import request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view()
def Index(request):
    return Response('Welcome to Divar Api HomePage')


@api_view(['GET'])
def Advertisements(request):
    return Response('Advertisements')


@api_view(['POST'])
def AddNewAdvertisement(request):
    return Response({"message": "{} is added".format(request.data['addvertisement_name'])}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def UpdateAdvertisement(request):
    return Response('UpdateAdvertisement')


@api_view(['POST'])
def RemoveAdvertisement(request):
    return Response('RemoveAdvertisement')
