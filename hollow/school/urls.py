from django.urls import path, re_path, include
from django.views.decorators.cache import cache_page
from .views import *
from rest_framework import routers

# routerSubject = routers.SimpleRouter()
# routerSubject.register(r'subject', SubjectViewSet)
# routerTerm = routers.SimpleRouter()
# routerTerm.register(r'term', TermViewSet)
# routerMarkType = routers.SimpleRouter()
# routerMarkType.register(r'marktype', MarkTypeViewSet)
# routerStudent = routers.SimpleRouter()
# routerStudent.register(r'student', StudentViewSet)
# routerTeacher = routers.SimpleRouter()
# routerTeacher.register(r'teacher', TeacherViewSet)
# routerMark = routers.SimpleRouter()
# routerMark.register(r'mark', MarkViewSet)

urlpatterns = [
    path('login/', LoginUser.as_view(), name='singIn'),
    path('logout/', signout_user, name='signOut'),
    path('register/', RegisterUser.as_view(), name='singUp'),
    path('', HomeView.as_view(), name='home'),
    path('about/', about, name='about'),
    path('term/<slug:term_slug>/', show_term, name='term'),
    path('courses/', CourseList.as_view(), name='courses'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('course/<slug:post_slug>', CourseDetail.as_view(), name='details'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('authorized/', Authorized_user, name='authorized'),
    path('canva/', Canva, name='canva'),
    path('task/', Task, name='task'),
    path('noncanva/', nonCanva, name='noncanva'),
    path('nonauthorized/', nonAuthorized_user, name='nonauthorized'),
    path('fullautho/', fullAuthorized_user, name='fullauthorized_user'),
    path('api/v1/subject/', SubjectAPIList.as_view()),
    path('api/v1/subject/<int:pk>/', SubjectAPIUpdate.as_view()),
    path('api/v1/subjectdelete/<int:pk>/', SubjectAPIDestroy.as_view()),
    path('api/v1/term/', TermAPIList.as_view()),
    path('api/v1/term/<int:pk>/', TermAPIUpdate.as_view()),
    path('api/v1/termdelete/<int:pk>/', TermAPIDestroy.as_view()),
    path('api/v1/marktype/', MarkTypeAPIList.as_view()),
    path('api/v1/marktype/<int:pk>/', MarkTypeAPIUpdate.as_view()),
    path('api/v1/marktypedelete/<int:pk>/', MarkTypeAPIDestroy.as_view()),
    path('api/v1/student/', StudentAPIList.as_view()),
    path('api/v1/student/<int:pk>/', StudentAPIUpdate.as_view()),
    path('api/v1/studentdelete/<int:pk>/', StudentAPIDestroy.as_view()),
    path('api/v1/teacher/', TeacherAPIList.as_view()),
    path('api/v1/teacher/<int:pk>/', TeacherAPIUpdate.as_view()),
    path('api/v1/teacherdelete/<int:pk>/', TeacherAPIDestroy.as_view()),
    path('api/v1/class/', ClassAPIList.as_view()),
    path('api/v1/class/<int:pk>/', ClassAPIUpdate.as_view()),
    path('api/v1/classdelete/<int:pk>/', ClassAPIDestroy.as_view()),
    path('api/v1/mark/', MarkAPIList.as_view()),
    path('api/v1/mark/<int:pk>/', MarkAPIUpdate.as_view()),
    path('api/v1/markdelete/<int:pk>/', MarkAPIDestroy.as_view()),
    # path('api/v1/subjectlist/', SubjectViewSet.as_view({'get': 'list'})),
    # path('api/v1/subjectlist/<int:pk>/', SubjectViewSet.as_view({'###': '###'})),
    # path('api/v1/marktypelist/', MarkTypeAPIView.as_view()),
    # path('api/v1/marktypelist/<int:pk>/', MarkTypeAPIView.as_view()),
    # path('api/v1/termlist/', TermsAPIView.as_view()),
    # path('api/v1/termlist/<int:pk>/', TermsAPIView.as_view()),
    # path('api/v1/termlist/', TermsAPIView.as_view()),
    # path('api/v1/studentlist/<int:pk>/', StudentAPIView.as_view()),
    # path('api/v1/studentlist/', StudentAPIView.as_view()),
    # path('api/v1/teacherlist/<int:pk>/', TeacherAPIView.as_view()),
    # path('api/v1/teacherlist/', TeacherAPIView.as_view()),
    # path('api/v1/classlist/<int:pk>/', ClassAPIView.as_view()),
    # path('api/v1/classlist/', ClassAPIView.as_view()),
    # path('api/v1/marklist/<int:pk>/', MarksAPIView.as_view()),
    # path('api/v1/marklist/', MarksAPIView.as_view())

]