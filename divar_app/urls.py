from django.urls import path
from divar_app.views import *

urlpatterns = [
    # API home page
    path("", Index),
    # get all Advertisements or get one Advertisement
    path("advertisements/", Advertisements),
    # create new advertisement
    path("advertisements/add_new/", AddNewAdvertisement),
    # update addvertisement
    path("advertisements/update/", UpdateAdvertisement),
    # delete addvertisement
    path("advertisements/remove/", RemoveAdvertisement)

]
