from django.urls import path, re_path
from django.views.decorators.cache import cache_page
from .views import *

urlpatterns = [
    path('login/', LoginUser.as_view(), name='singIn'),
    path('logout/', signout_user, name='signOut'),
    path('register/', RegisterUser.as_view(), name='singUp'),
    path('', HomeView.as_view(), name='home'),
    path('about/', about, name='about'),
    path('term/<slug:term_slug>/', show_term, name='term'),
    path('courses/', CourseList.as_view(), name='courses'),
    path('contact/', contact, name='contact'),
    path('details/', Details, name='details'),
    path('profile/', Profile, name='profile')


]