from django.db import models


class MarkType(models.Model):
    MarkType = models.CharField(max_length=255, verbose_name='Тип задания')
    TypeName = models.CharField(max_length=255, verbose_name='Название задания')

    def __str__(self):
        return self.TypeName

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
        ordering = ['id']


class Terms(models.Model):
    TermName = models.CharField(max_length=255, verbose_name='Название семестра')

    def __str__(self):
        return self.TermName

    class Meta:
        verbose_name = 'Семестр'
        verbose_name_plural = 'Семестры'
        ordering = ['id']


class Subjects(models.Model):
    SubjectName = models.CharField(max_length=255, verbose_name='Название занятия')
    TermId = models.ForeignKey(Terms, on_delete=models.CASCADE, verbose_name='К какому семестру')

    def __str__(self):
        return self.SubjectName

    class Meta:
        verbose_name = 'Занятие'
        verbose_name_plural = 'Занятия'
        ordering = ['id']


class PersonType(models.Model):
    Prsntype = models.CharField(max_length=255, verbose_name='Тип')

    def __str__(self):
        return self.Prsntype

    class Meta:
        verbose_name = 'Тип персоны'
        verbose_name_plural = 'Тип персон'
        ordering = ['id']


class Person(models.Model):
    PrsnFristName = models.CharField(max_length=255, verbose_name='Имя')
    PrsnScndName = models.CharField(max_length=255, verbose_name='Фамилия')
    PrsnThrdName = models.CharField(max_length=255, verbose_name='Отчество')
    PrsnDOB = models.DateField(verbose_name='Дата рождения')
    PrsnType = models.ForeignKey(PersonType, on_delete=models.CASCADE, verbose_name='Принадлежность')

    def __str__(self):
        return self.PrsnFristName

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'
        ordering = ['id']


class Marks(models.Model):
    SubjectId = models.ForeignKey(Subjects, on_delete=models.CASCADE, verbose_name='Занятие')
    PrsnId = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name='Ученик')
    Mark = models.IntegerField(verbose_name='Оценка')
    MarkType = models.ForeignKey(MarkType, on_delete=models.CASCADE, verbose_name='Задание')

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'
        ordering = ['id']


class StudentData(models.Model):
    StdName = models.CharField(max_length=255, verbose_name='Имя студента')
    StdDOB = models.DateField(verbose_name='День рождения')
    StdJoinDate = models.DateField(verbose_name='Дата зачисления')
    PrsnId = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name='Персона')
    StdAddress = models.CharField(max_length=255, verbose_name='Место жительства')

    def __str__(self):
        return self.StdName

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        ordering = ['id']


class Class(models.Model):
    ClassName = models.CharField(max_length=255, verbose_name='Название группы')
    StdId = models.ForeignKey(StudentData, on_delete=models.CASCADE, verbose_name='Студент')
    SubjectId = models.ForeignKey(Subjects, on_delete=models.CASCADE, verbose_name='Занятие')


    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        ordering = ['id']
