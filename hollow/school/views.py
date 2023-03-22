from django.http import HttpResponse, HttpResponseNotFound, HttpResponseServerError, HttpResponseBadRequest, \
    HttpResponseForbidden
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import *

menu = ["Войти", "Регистрация"]


def form(request):
    return render(request, 'school/form.html')


def index(request):
    return render(request, 'school/index.html', {'menu': menu, 'title': 'Главная страница'})
def courses(request):
    return render(request, 'school/courses.html')


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
