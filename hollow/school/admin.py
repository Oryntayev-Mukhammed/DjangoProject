from django.contrib import admin
from .models import *


class TermsAdmin(admin.ModelAdmin):
    list_display = ['id', 'TermName']
    list_display_links = ['id', 'TermName']
    search_fields = ['TermName']
    prepopulated_fields = {"slug": ("TermName",)}


class MarkTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'MarkType', 'TypeName']
    list_display_links = ['id', 'MarkType']
    search_fields = ['TypeName']
    list_filter = ['MarkType']
    prepopulated_fields = {"slug": ("TypeName",)}


class SubjectsAdmin(admin.ModelAdmin):
    list_display = ['id', 'SubjectName', 'TermId']
    list_display_links = ['id', 'SubjectName']
    search_fields = ['SubjectName']
    list_filter = ['TermId']
    prepopulated_fields = {"slug": ("SubjectName",)}


class PersonTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'Prsntype']
    list_display_links = ['id', 'Prsntype']
    prepopulated_fields = {"slug": ("Prsntype",)}


class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'PrsnFristName', 'PrsnScndName', 'PrsnThrdName', 'PrsnDOB', 'PrsnType']
    list_display_links = ['id', 'PrsnFristName']
    search_fields = ['PrsnFristName']
    list_filter = ['PrsnType']
    prepopulated_fields = {"slug": ("PrsnFristName",)}


class MarksAdmin(admin.ModelAdmin):
    list_display = ['id', 'SubjectId', 'PrsnId', 'Mark', 'MarkType']
    list_display_links = ['id', 'SubjectId']
    search_fields = ['SubjectId', 'PrsnId', 'MarkType']
    list_filter = ['SubjectId', 'MarkType']
    prepopulated_fields = {"slug": ("Mark",)}


class StudentDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'StdName', 'StdDOB', 'StdJoinDate', 'PrsnId', 'StdAddress']
    list_display_links = ['id', 'StdName']
    search_fields = ['StdName']
    prepopulated_fields = {"slug": ("StdName",)}


class ClassAdmin(admin.ModelAdmin):
    list_display = ['id', 'ClassName', 'StdId', 'SubjectId']
    list_display_links = ['id', 'ClassName']
    search_fields = ['ClassName']
    list_filter = ['SubjectId']
    prepopulated_fields = {"slug": ("ClassName",)}


admin.site.register(Terms, TermsAdmin)
admin.site.register(MarkType, MarkTypeAdmin)
admin.site.register(Subjects, SubjectsAdmin)
admin.site.register(PersonType, PersonTypeAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Marks, MarksAdmin)
admin.site.register(StudentData, StudentDataAdmin)
admin.site.register(Class, ClassAdmin)