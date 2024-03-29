from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.forms import model_to_dict
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseServerError, HttpResponseBadRequest, \
    HttpResponseForbidden
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from rest_framework import generics, status, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated

from .forms import *
from .models import *
from django.views.generic import ListView, CreateView, FormView, DetailView

from .permissions import IsAdminOrReadOnly
from .serializer import SubjectsSerializer, MarkTypeSerializer, TermsSerializer, StudentSerializer, TeacherSerializer, \
    ClassSerializer, MarksSerializer, ApplyCourseSerializer
from .utils import *
from .templatetags.school_tags import *
from django.contrib.auth.mixins import LoginRequiredMixin


def Profile(request):
    return render(request, 'school/profile.html')

def nonCanva(request):
    return render(request, 'school/noncanva.html')

def Task(request):
    return render(request, 'school/task.html')

def Canva(request):
    return render(request, 'school/canva.html')

def fullAuthorized_user(request):
    return render(request, 'school/fullauthorized_user.html')

def nonAuthorized_user(request):
    return render(request, 'school/nonauthorized_user.html')

def Authorized_user(request):
    return render(request, 'school/authorized_user.html')


class CourseList(DataMixin, ListView):
    paginate_by = 6
    model = Subjects
    template_name = 'school/courses.html'
    context_object_name = 'courses'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Курсы")
        return dict(list(context.items()) + list(c_def.items()))


class CourseDetail(DetailView):
    model = Subjects
    template_name = 'school/details.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'course'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class HomeView(DataMixin, ListView):
    model = Subjects
    template_name = 'school/index.html'
    context_object_name = 'courses'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['last_item'] = get_last_course()
        context['last_three_items'] = get_last_three_course()
        c_def = self.get_user_context(title="OSI")
        return dict(list(context.items()) + list(c_def.items()))


class ProfileView(DataMixin, ListView):
    model = Subjects
    template_name = 'school/profile.html'
    context_object_name = 'profile'

    def get_context_data(self, *, object_list=None, **kwargs):
        if self.request.user.is_authenticated:
            context = super().get_context_data(**kwargs)
            context['student'] = get_student(self.request.user.id)
            context['sertificates'] = get_sertificate(self.request.user.id)
            return dict(list(context.items()))
        else:
            self.template_name = 'school/about.html'
            context = super().get_context_data(**kwargs)
            return dict(list(context.items()))

def Details(request):
    return render(request, 'school/details.html')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'school/form2.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'school/form.html'
    success_url = reverse_lazy('singIn')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


def signout_user(request):
    logout(request)
    return redirect('home')


class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'school/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Обратная связь")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')

class SubjectApiListPagination(PageNumberPagination):
    page_size = 6
    page_query_param = 'page_size'
    max_page_size = 10

class SubjectAPIList(generics.ListCreateAPIView):
    queryset = Subjects.objects.all()
    serializer_class = SubjectsSerializer
    pagination_class = SubjectApiListPagination
class SubjectAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Subjects.objects.all()
    serializer_class = SubjectsSerializer
    permission_classes = (IsAdminOrReadOnly, )
class SubjectAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Subjects.objects.all()
    serializer_class = SubjectsSerializer
    permission_classes = (IsAdminOrReadOnly, )

class TermAPIList(generics.ListCreateAPIView):
    queryset = Terms.objects.all()
    serializer_class = TermsSerializer
class TermAPIUpdate(generics.ListCreateAPIView):
    queryset = Terms.objects.all()
    serializer_class = TermsSerializer
    permission_classes = (IsAdminOrReadOnly,)
class TermAPIDestroy(generics.ListCreateAPIView):
    queryset = Terms.objects.all()
    serializer_class = TermsSerializer
    permission_classes = (IsAdminOrReadOnly,)

class MarkTypeAPIList(generics.ListCreateAPIView):
    queryset = MarkType.objects.all()
    serializer_class = MarkTypeSerializer
class MarkTypeAPIUpdate(generics.ListCreateAPIView):
    queryset = MarkType.objects.all()
    serializer_class = MarkTypeSerializer
    permission_classes = (IsAdminOrReadOnly,)
class MarkTypeAPIDestroy(generics.ListCreateAPIView):
    queryset = MarkType.objects.all()
    serializer_class = MarkTypeSerializer
    permission_classes = (IsAdminOrReadOnly,)

class StudentAPIList(generics.ListCreateAPIView):
    queryset = StudentData.objects.all()
    serializer_class = StudentSerializer
class StudentAPIUpdate(generics.ListCreateAPIView):
    queryset = StudentData.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (IsAdminOrReadOnly,)
class StudentAPIDestroy(generics.ListCreateAPIView):
    queryset = StudentData.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (IsAdminOrReadOnly,)

class TeacherAPIList(generics.ListCreateAPIView):
    queryset = TeacherData.objects.all()
    serializer_class = TeacherSerializer
class TeacherAPIUpdate(generics.ListCreateAPIView):
    queryset = TeacherData.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = (IsAdminOrReadOnly,)
class TeacherAPIDestroy(generics.ListCreateAPIView):
    queryset = TeacherData.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = (IsAdminOrReadOnly,)

class ClassAPIList(generics.ListCreateAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
class ClassAPIUpdate(generics.ListCreateAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = (IsAdminOrReadOnly,)
class ClassAPIDestroy(generics.ListCreateAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = (IsAdminOrReadOnly,)

class MarkAPIList(generics.ListCreateAPIView):
    queryset = Marks.objects.all()
    serializer_class = MarksSerializer
class MarkAPIUpdate(generics.ListCreateAPIView):
    queryset = Marks.objects.all()
    serializer_class = MarksSerializer
    permission_classes = (IsAdminOrReadOnly,)
class MarkAPIDestroy(generics.ListCreateAPIView):
    queryset = Marks.objects.all()
    serializer_class = MarksSerializer
    permission_classes = (IsAdminOrReadOnly,)

class MarkViewSet(viewsets.ModelViewSet):
    queryset = Marks.objects.all()
    serializer_class = MarksSerializer

class ApplyCoursePagination(PageNumberPagination):
    page_size = 6
    page_query_param = 'page_size'
    max_page_size = 10

class ApplyCourseAPIList(generics.ListCreateAPIView):
    queryset = ApplyCourse.objects.all()
    serializer_class = ApplyCourseSerializer
    pagination_class = ApplyCoursePagination
class ApplyCourseAPIUpdate(generics.ListCreateAPIView):
    queryset = ApplyCourse.objects.all()
    serializer_class = ApplyCourseSerializer
    permission_classes = (IsAdminOrReadOnly,)
class ApplyCourseAPIDestroy(generics.ListCreateAPIView):
    queryset = ApplyCourse.objects.all()
    serializer_class = ApplyCourseSerializer
    permission_classes = (IsAdminOrReadOnly,)

def about(request):
    return render(request, 'school/about.html')


def show_term(request, term_slug):
    term = get_object_or_404(Terms, slug=term_slug)
    context = {
        'TermName': term.TermName,
    }

    return render(request, 'school/term.html', context=context)


def categories(request, catid):
    if request.GET:
        print(request.GET)

    return HttpResponse(f"<h1>Статьи</h1><p>{catid}</p>")


def archive(request, year):
    if int(year) > 2023:
        raise Http404()
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


# class SubjectsAPIView(APIView):
#     def get(self, request):
#         w = Subjects.objects.all()
#         return Response({'subjects': SubjectsSerializer(w, many=True).data})
#
#     def post(self, request):
#
#         serializer = SubjectsSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'Subjects': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         try:
#             instance = Subjects.objects.get(pk=pk)
#         except Subjects.DoesNotExist:
#             return Response({"error": "Subject does not exist"}, status=status.HTTP_404_NOT_FOUND)
#
#         serializer = SubjectsSerializer(instance, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#
#     def delete(self, request, pk):
#         subject = Subjects.objects.get(pk=pk)
#         subject.delete()
#         return Response({'message': 'Subject has been deleted.'})


# class TermsAPIView(APIView):
#     def get(self, request):
#         w = Terms.objects.all()
#         return Response({'Terms': TermsSerializer(w, many=True).data})
#
#     def post(self, request):
#
#         serializer = TermsSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'Terms': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         try:
#             instance = Terms.objects.get(pk=pk)
#         except Terms.DoesNotExist:
#             return Response({"error": "Term does not exist"}, status=status.HTTP_404_NOT_FOUND)
#
#         serializer = TermsSerializer(instance, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#
#     def delete(self, request, pk):
#         subject = Terms.objects.get(pk=pk)
#         subject.delete()
#         return Response({'message': 'Term has been deleted.'})


# class MarkTypeAPIView(APIView):
#     def get(self, request):
#         w = MarkType.objects.all()
#         return Response({'MarkTypes': MarkTypeSerializer(w, many=True).data})
#
#     def post(self, request):
#
#         serializer = MarkTypeSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'MarkTypes': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         try:
#             instance = MarkType.objects.get(pk=pk)
#         except MarkType.DoesNotExist:
#             return Response({"error": "MarkType does not exist"}, status=status.HTTP_404_NOT_FOUND)
#
#         serializer = MarkTypeSerializer(instance, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#
#     def delete(self, request, pk):
#         subject = MarkType.objects.get(pk=pk)
#         subject.delete()
#         return Response({'message': 'MarkType has been deleted.'})


# class StudentAPIView(APIView):
#     def get(self, request):
#         w = StudentData.objects.all()
#         return Response({'Students': TermsSerializer(w, many=True).data})
#
#     def post(self, request):
#
#         serializer = StudentSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'Students': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         try:
#             instance = StudentData.objects.get(pk=pk)
#         except StudentData.DoesNotExist:
#             return Response({"error": "Student does not exist"}, status=status.HTTP_404_NOT_FOUND)
#
#         serializer = StudentSerializer(instance, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#
#     def delete(self, request, pk):
#         subject = StudentData.objects.get(pk=pk)
#         subject.delete()
#         return Response({'message': 'Student has been deleted.'})


# class TeacherAPIView(APIView):
#     def get(self, request):
#         w = TeacherData.objects.all()
#         return Response({'Teachers': TeacherSerializer(w, many=True).data})
#
#     def post(self, request):
#
#         serializer = TeacherSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'Teachers': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         try:
#             instance = TeacherData.objects.get(pk=pk)
#         except TeacherData.DoesNotExist:
#             return Response({"error": "Teacher does not exist"}, status=status.HTTP_404_NOT_FOUND)
#
#         serializer = TeacherSerializer(instance, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#
#     def delete(self, request, pk):
#         subject = TeacherData.objects.get(pk=pk)
#         subject.delete()
#         return Response({'message': 'Teacher has been deleted.'})


# class ClassAPIView(APIView):
#     def get(self, request):
#         w = Class.objects.all()
#         return Response({'Classes': ClassSerializer(w, many=True).data})
#
#     def post(self, request):
#
#         serializer = ClassSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'Classes': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         try:
#             instance = Class.objects.get(pk=pk)
#         except Class.DoesNotExist:
#             return Response({"error": "Class does not exist"}, status=status.HTTP_404_NOT_FOUND)
#
#         serializer = ClassSerializer(instance, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#
#     def delete(self, request, pk):
#         subject = Class.objects.get(pk=pk)
#         subject.delete()
#         return Response({'message': 'Class has been deleted.'})


# class MarksAPIView(APIView):
#     def get(self, request):
#         w = Marks.objects.all()
#         return Response({'Marks': ClassSerializer(w, many=True).data})
#
#     def post(self, request):
#
#         serializer = MarksSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'Marks': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         try:
#             instance = Marks.objects.get(pk=pk)
#         except Marks.DoesNotExist:
#             return Response({"error": "Mark does not exist"}, status=status.HTTP_404_NOT_FOUND)
#
#         serializer = MarkSerializer(instance, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#
#     def delete(self, request, pk):
#         subject = Mark.objects.get(pk=pk)
#         subject.delete()
#         return Response({'message': 'Mark has been deleted.'})

#class SubjectsAPIView(generics.ListAPIView):
#    queryset = Subjects.objects.all()
#    serializer_class = SubjectsSerializer


def serverError(request):
    return HttpResponseServerError('<h1>Проблема с сервером</h1>')


def badRequest(request, exception):
    return HttpResponseBadRequest('<h1>Ошибка данных</h1>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def forbiddenRequest(request, exception):
    return HttpResponseForbidden('<h1>Ошибка доступа</h1>')
