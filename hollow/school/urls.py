from django.urls import path, re_path, include
from django.views.decorators.cache import cache_page
from .views import *
from rest_framework import routers

# routerSubject = routers.SimpleRouter()
# routerSubject.register(r'subject', SubjectViewSet)
routerTerm = routers.SimpleRouter()
routerTerm.register(r'term', TermViewSet)
routerMarkType = routers.SimpleRouter()
routerMarkType.register(r'marktype', MarkTypeViewSet)
routerStudent = routers.SimpleRouter()
routerStudent.register(r'student', StudentViewSet)
routerTeacher = routers.SimpleRouter()
routerTeacher.register(r'teacher', TeacherViewSet)
routerClass = routers.SimpleRouter()
routerClass.register(r'class', ClassViewSet)
routerMark = routers.SimpleRouter()
routerMark.register(r'mark', MarkViewSet)

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
    path('api/v1/subject/<int:pk>', SubjectAPIUpdate.as_view()),
    path('api/v1/subjectdelete/<int:pk>/', SubjectAPIDestroy.as_view()),
    path('api/v1/', include(routerTerm.urls)),
    path('api/v1/', include(routerMarkType.urls)),
    path('api/v1/', include(routerStudent.urls)),
    path('api/v1/', include(routerTeacher.urls)),
    path('api/v1/', include(routerClass.urls)),
    path('api/v1/', include(routerMark.urls)),
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