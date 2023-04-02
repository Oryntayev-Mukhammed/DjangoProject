from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseServerError, HttpResponseBadRequest, \
    HttpResponseForbidden
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from .forms import *
from .models import *
from django.views.generic import ListView, CreateView
from .utils import *
from .templatetags.school_tags import *
from django.contrib.auth.mixins import LoginRequiredMixin


def Profile(request):
    return render(request, 'school/profile.html')


class CourseList(DataMixin, ListView):
    paginate_by = 6
    model = Subjects
    template_name = 'school/courses.html'
    context_object_name = 'courses'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Курсы")
        return dict(list(context.items()) + list(c_def.items()))


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


def contact(request):
    return render(request, 'school/contact.html')


def about(request):
    return render(request, 'school/about.html')


def show_term(request, term_slug):
    term = get_object_or_404(Terms, slug=term_slug)
    context = {
        'TermName' : term.TermName,
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


def serverError(request):
    return HttpResponseServerError('<h1>Проблема с сервером</h1>')


def badRequest(request, exception):
    return HttpResponseBadRequest('<h1>Ошибка данных</h1>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def forbiddenRequest(request, exception):
    return HttpResponseForbidden('<h1>Ошибка доступа</h1>')
