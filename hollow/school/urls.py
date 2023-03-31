from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', SingIn, name='singIn'),
    path('register/', SingUp, name='singUp'),
    path('index/', HomeView.as_view(), name='home'),
    path('about/', about, name='about'),
    path('term/<slug:term_slug>/', show_term, name='term'),
    path('courses/', CourseList.as_view(), name='courses'),
    path('contact/', contact, name='contact'),
    path('details/', Details, name='details'),
    path('profile/', Profile, name='profile')


]