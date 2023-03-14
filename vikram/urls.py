from vikram.views import *
from django.urls import path
app_name='nothing'
urlpatterns=[
    path('vikram/',vikram,name='vikram'),
]