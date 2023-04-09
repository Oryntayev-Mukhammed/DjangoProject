from django.contrib import admin
from .models import *


class TermsAdmin(admin.ModelAdmin):
    list_display = ['id', 'TermName', 'time_create', 'time_update']
    list_display_links = ['id', 'TermName']
    search_fields = ['TermName']
    prepopulated_fields = {"slug": ("TermName",)}
    readonly_fields = ('time_create', 'time_update')


class MarkTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'MarkType', 'TypeName', 'time_create', 'time_update']
    list_display_links = ['id', 'MarkType']
    search_fields = ['TypeName']
    list_filter = ['MarkType']
    prepopulated_fields = {"slug": ("TypeName",)}
    readonly_fields = ('time_create', 'time_update')


class SubjectsAdmin(admin.ModelAdmin):
    list_display = ['id', 'SubjectName', 'Text', 'Duration', 'TermId', 'time_create', 'time_update']
    list_display_links = ['id', 'SubjectName']
    search_fields = ['SubjectName']
    list_filter = ['TermId']
    prepopulated_fields = {"slug": ("SubjectName",)}
    readonly_fields = ('time_create', 'time_update')


class PersonTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'Prsntype', 'time_create', 'time_update']
    list_display_links = ['id', 'Prsntype']
    prepopulated_fields = {"slug": ("Prsntype",)}
    readonly_fields = ('time_create', 'time_update')


class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'PrsnFristName', 'PrsnScndName', 'PrsnThrdName', 'PrsnDOB', 'PrsnType', 'time_create', 'time_update']
    list_display_links = ['id', 'PrsnFristName']
    search_fields = ['PrsnFristName']
    list_filter = ['PrsnType']
    prepopulated_fields = {"slug": ("PrsnFristName",)}
    readonly_fields = ('time_create', 'time_update')


class MarksAdmin(admin.ModelAdmin):
    list_display = ['id', 'SubjectId', 'PrsnId', 'Mark', 'MarkType', 'time_create', 'time_update']
    list_display_links = ['id', 'SubjectId']
    search_fields = ['SubjectId', 'PrsnId', 'MarkType']
    list_filter = ['SubjectId', 'MarkType']
    prepopulated_fields = {"slug": ("Mark",)}
    readonly_fields = ('time_create', 'time_update')


class StudentDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'StdName', 'StdDOB', 'StdJoinDate', 'PrsnId', 'StdAddress', 'time_create', 'time_update']
    list_display_links = ['id', 'StdName']
    search_fields = ['StdName']
    prepopulated_fields = {"slug": ("StdName",)}
    readonly_fields = ('time_create', 'time_update')


class ClassAdmin(admin.ModelAdmin):
    list_display = ['id', 'ClassName', 'StdId', 'SubjectId', 'time_create', 'time_update']
    list_display_links = ['id', 'ClassName']
    search_fields = ['ClassName']
    list_filter = ['SubjectId']
    prepopulated_fields = {"slug": ("ClassName",)}
    readonly_fields = ('time_create', 'time_update')


admin.site.register(Terms, TermsAdmin)
admin.site.register(MarkType, MarkTypeAdmin)
admin.site.register(Subjects, SubjectsAdmin)
admin.site.register(PersonType, PersonTypeAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Marks, MarksAdmin)
admin.site.register(StudentData, StudentDataAdmin)
admin.site.register(Class, ClassAdmin)