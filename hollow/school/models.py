from django.db import models


class MarkType(models.Model):
    MarkType = models.CharField(max_length=255)
    TypeName = models.CharField(max_length=255)


class Terms(models.Model):
    TermName = models.CharField(max_length=255)


class Subjects(models.Model):
    SubjectName = models.CharField(max_length=255)
    TermId = models.ForeignKey(Terms, on_delete=models.CASCADE)


class PersonType(models.Model):
    Prsntype = models.CharField(max_length=255)


class Person(models.Model):
    PrsnFristName = models.CharField(max_length=255)
    PrsnScndName = models.CharField(max_length=255)
    PrsnThrdName = models.CharField(max_length=255)
    PrsnDOB = models.CharField(max_length=255)
    PrsnType = models.ForeignKey(PersonType, on_delete=models.CASCADE)


class Marks(models.Model):
    SubjectId = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    PrsnId = models.ForeignKey(Person, on_delete=models.CASCADE)
    Mark = models.IntegerField(max_length=255)
    MarkType = models.ForeignKey(MarkType, on_delete=models.CASCADE)


class StudentData(models.Model):
    StdName = models.CharField(max_length=255)
    StdDOB = models.CharField(max_length=255)
    StdJoinDate = models.DateField()
    PrsnId = models.ForeignKey(Person, on_delete=models.CASCADE)
    StdAddress = models.CharField(max_length=255)


class Class(models.Model):
    ClassName = models.CharField(max_length=255)
    StdId = models.ForeignKey(StudentData, on_delete=models.CASCADE)
