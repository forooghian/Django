from urllib import request
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def Index(request):
    return Response('<center><h1>Welcome to Divar Api HomePage</h1></center>')


@api_view(['GET', 'POST'])
def Advertisements(request):
    pass


@api_view(['POST'])
def AddNewAdvertisement(request):
    pass


@api_view(['PUT'])
def UpdateAdvertisement(request):
    pass


@api_view(['POST'])
def RemoveAdvertisement(request):
    pass
