from django.contrib import admin
from .models import *


class TermsAdmin(admin.ModelAdmin):
    list_display = ['id', 'TermName']
    list_display_links = ['id', 'TermName']
    search_fields = ['TermName']


class MarkTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'MarkType', 'TypeName']
    list_display_links = ['id', 'MarkType']
    search_fields = ['TypeName']
    list_filter = ['MarkType']


class SubjectsAdmin(admin.ModelAdmin):
    list_display = ['id', 'SubjectName', 'TermId']
    list_display_links = ['id', 'SubjectName']
    search_fields = ['SubjectName']
    list_filter = ['TermId']


class PersonTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'Prsntype']
    list_display_links = ['id', 'Prsntype']


class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'PrsnFristName', 'PrsnScndName', 'PrsnThrdName', 'PrsnDOB', 'PrsnType']
    list_display_links = ['id', 'PrsnFristName']
    search_fields = ['PrsnFristName']
    list_filter = ['PrsnType']


class MarksAdmin(admin.ModelAdmin):
    list_display = ['id', 'SubjectId', 'PrsnId', 'Mark', 'MarkType']
    list_display_links = ['id', 'SubjectId']
    search_fields = ['SubjectId', 'PrsnId', 'MarkType']
    list_filter = ['SubjectId', 'PrsnId', 'MarkType']


class StudentDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'StdName', 'StdDOB', 'StdJoinDate', 'PrsnId', 'StdAddress']
    list_display_links = ['id', 'StdName']
    search_fields = ['StdName']


class ClassAdmin(admin.ModelAdmin):
    list_display = ['id', 'ClassName', 'StdId', 'SubjectId']
    list_display_links = ['id', 'ClassName']
    search_fields = ['ClassName']
    list_filter = ['StdId']


admin.site.register(Terms, TermsAdmin)
admin.site.register(MarkType, MarkTypeAdmin)
admin.site.register(Subjects, SubjectsAdmin)
admin.site.register(PersonType, PersonTypeAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Marks, MarksAdmin)
admin.site.register(StudentData, StudentDataAdmin)
admin.site.register(Class, ClassAdmin)