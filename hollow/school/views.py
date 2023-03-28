from django.http import HttpResponse, HttpResponseNotFound, HttpResponseServerError, HttpResponseBadRequest, \
    HttpResponseForbidden
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import *
from django.views.generic import ListView
from .utils import *
from .templatetags.school_tags import *
from django.contrib.auth.mixins import LoginRequiredMixin


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

def SingIn(request):
    return render(request, 'school/form2.html')


def SingUp(request):
    return render(request, 'school/form.html')

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
