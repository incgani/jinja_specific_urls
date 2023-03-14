from khaidi.views import *
from django.urls import path
app_name='something'
urlpatterns=[
    path('khaidi/',khaidi,name='khaidi'),
]