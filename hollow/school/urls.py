from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', form, name='form'),
    path('index/', index)

]