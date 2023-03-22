from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', form, name='form'),
    path('index/', index, name='home'),
    path('about/', about, name='about'),
    path('term/<slug:term_slug>/', show_term, name='term'),
   path('courses/', courses, name='courses')

]