from django.urls import path
from . import viwes
urlpatterns = [
    path('',viwes.Home, name='home'),
    path('about/',viwes.about,name='about'),
    path('contact/',viwes.contact,name='contact'),
]