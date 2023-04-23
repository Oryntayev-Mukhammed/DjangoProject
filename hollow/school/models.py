from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class MarkType(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, null=True, verbose_name='URL')
    MarkType = models.CharField(max_length=255, verbose_name='Тип задания')
    TypeName = models.CharField(max_length=255, verbose_name='Название задания')
    time_create = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, null=True, verbose_name="Время изменения")

    def __str__(self):
        return self.TypeName

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
        ordering = ['id']


class Terms(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, null=True, verbose_name='URL')
    TermName = models.CharField(max_length=255, verbose_name='Название семестра')
    time_create = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, null=True, verbose_name="Время изменения")

    def __str__(self):
        return self.TermName

    class Meta:
        verbose_name = 'Семестр'
        verbose_name_plural = 'Семестры'
        ordering = ['id']


class Subjects(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, null=True, verbose_name='URL')
    SubjectName = models.CharField(max_length=255, verbose_name='Название занятия')
    Text = models.TextField(verbose_name='Описание занятия')
    Duration = models.IntegerField(verbose_name='Время обучения в неделях')
    TermId = models.ForeignKey(Terms, on_delete=models.CASCADE, verbose_name='К какому семестру')
    Price = models.IntegerField(verbose_name='Цена')
    time_create = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, null=True, verbose_name="Время изменения")

    def __str__(self):
        return self.SubjectName

    class Meta:
        verbose_name = 'Занятие'
        verbose_name_plural = 'Занятия'
        ordering = ['id']


class StudentData(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, null=True, verbose_name='URL')
    StdName = models.CharField(null=True, max_length=255, verbose_name='Имя')
    StdScndName = models.CharField(null=True, max_length=255, verbose_name='Фамилия')
    StdThrdName = models.CharField(null=True, max_length=255, verbose_name='Отчество')
    StdDOB = models.DateField(null=True, verbose_name='Дата рождения')
    PhoneNumber = PhoneNumberField(null=True, verbose_name='Номер телефона')
    StdJoinDate = models.DateField(null=True, verbose_name='Дата зачисления')
    StdAddress = models.CharField(null=True, max_length=255, verbose_name='Место жительства')
    UserId = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    discript = models.CharField(null=True, max_length=255, verbose_name='Ваше поле')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")

    def __str__(self):
        return self.StdName

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        ordering = ['id']


class TeacherData(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, null=True, verbose_name='URL')
    TName = models.CharField(max_length=255, verbose_name='Имя')
    TScndName = models.CharField(max_length=255, verbose_name='Фамилия')
    TThrdName = models.CharField(max_length=255, verbose_name='Отчество')
    TDOB = models.DateField(verbose_name='Дата рождения')
    TJoinDate = models.DateField(verbose_name='Дата зачисления')
    TAddress = models.CharField(max_length=255, verbose_name='Место жительства')
    UserId = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    time_create = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, null=True, verbose_name="Время изменения")

    def __str__(self):
        return self.TName

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'
        ordering = ['id']


class Class(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, null=True, verbose_name='URL')
    ClassName = models.CharField(max_length=255, verbose_name='Название группы')
    StdId = models.ForeignKey(StudentData, on_delete=models.CASCADE, verbose_name='Студент')
    SubjectId = models.ForeignKey(Subjects, on_delete=models.CASCADE, verbose_name='Занятие')
    TeacherId = models.ForeignKey(TeacherData, on_delete=models.CASCADE, verbose_name='Учитель')
    time_create = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, null=True, verbose_name="Время изменения")


    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        ordering = ['id']


class Marks(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, null=True, verbose_name='URL')
    SubjectId = models.ForeignKey(Subjects, on_delete=models.CASCADE, verbose_name='Занятие')
    ClassId = models.ForeignKey(Class, on_delete=models.CASCADE, verbose_name='Номер группы')
    StudentId = models.ForeignKey(StudentData, on_delete=models.CASCADE, verbose_name='Ученик')
    Mark = models.IntegerField(verbose_name='Оценка')
    MarkType = models.ForeignKey(MarkType, on_delete=models.CASCADE, verbose_name='Тип Задания')
    time_create = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, null=True, verbose_name="Время изменения")

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'
        ordering = ['id']


class ApplyCourse(models.Model):
    UserId = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    SubjectId = models.ForeignKey(Subjects, on_delete=models.CASCADE, verbose_name='Занятие')
    is_valid = models.BooleanField(verbose_name='Действителен ли сертификат')
    time_create = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, null=True, verbose_name="Время изменения")

    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'
        ordering = ['id']