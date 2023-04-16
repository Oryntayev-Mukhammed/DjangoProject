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
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('details/', Details, name='details'),
    path('profile/', Profile, name='profile'),
    path('api/v1/subjectlist/', SubjectsAPIView.as_view()),
    path('api/v1/subjectlist/<int:pk>/', SubjectsAPIView.as_view()),
    path('api/v1/marktypelist/', MarkTypeAPIView.as_view()),
    path('api/v1/marktypelist/<int:pk>/', MarkTypeAPIView.as_view()),
    path('api/v1/termlist/', TermsAPIView.as_view()),
    path('api/v1/termlist/<int:pk>/', TermsAPIView.as_view()),
    path('api/v1/termlist/', TermsAPIView.as_view()),
    path('api/v1/studentlist/<int:pk>/', StudentAPIView.as_view()),
    path('api/v1/studentlist/', StudentAPIView.as_view()),
    path('api/v1/teacherlist/<int:pk>/', TeacherAPIView.as_view()),
    path('api/v1/teacherlist/', TeacherAPIView.as_view()),
    path('api/v1/classlist/<int:pk>/', ClassAPIView.as_view()),
    path('api/v1/classlist/', ClassAPIView.as_view()),
    path('api/v1/marklist/<int:pk>/', MarksAPIView.as_view()),
    path('api/v1/marklist/', MarksAPIView.as_view())

]