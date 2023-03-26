from .models import *
menu = [{'title': "OSI", 'url_name': 'index'},
        {'title': "Курсы", 'url_name': 'courses'},
        {'title': "Контакты", 'url_name': 'contact'},
        {'title': "Вход", 'url_name': ''},
        {'title': "Регистрация", 'url_name': 'register'}
]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context