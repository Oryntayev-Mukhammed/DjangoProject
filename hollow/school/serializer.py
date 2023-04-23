import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import *


# class SubjectModel:
#     def __init__(self, SubjectName, Text, Duration, TermId):
#         self.SubjectName = SubjectName
#         self.Text = Text
#         self.Duration = Duration
#         self.TermId = TermId

class TermsSerializer(serializers.Serializer):
    TermName = serializers.CharField(max_length=255)
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Terms.objects.create(**validated_data)

    def update(self, instance, validate_data):
        for attr, value in validate_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class MarkTypeSerializer(serializers.Serializer):
    MarkType = serializers.CharField(max_length=255)
    TypeName = serializers.CharField(max_length=255)
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return MarkType.objects.create(**validated_data)

    def update(self, instance, validate_data):
        for attr, value in validate_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class SubjectsSerializer(serializers.Serializer):
    SubjectName = serializers.CharField(max_length=255)
    Price = serializers.IntegerField()
    Text = serializers.CharField()
    Duration = serializers.IntegerField()
    TermId = serializers.PrimaryKeyRelatedField(queryset=Terms.objects.values_list('id', flat=True))
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        term_id = validated_data.pop('TermId')
        term = Terms.objects.get(id=term_id)
        return Subjects.objects.create(TermId=term, **validated_data)

    def update(self, instance, validate_data):
        term_id = validate_data.pop('TermId')
        term = Terms.objects.get(id=term_id)
        instance.TermId = term
        for attr, value in validate_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class StudentSerializer(serializers.Serializer):
    StdName = serializers.CharField(max_length=255)
    StdScndName = serializers.CharField(max_length=255)
    StdThrdName = serializers.CharField(max_length=255)
    StdDOB = serializers.DateTimeField()
    StdJoinDate = serializers.DateTimeField()
    StdAddress = serializers.CharField(max_length=255)
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return StudentData.objects.create(**validated_data)

    def update(self, instance, validate_data):
        for attr, value in validate_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class TeacherSerializer(serializers.Serializer):
    TName = serializers.CharField(max_length=255)
    TScndName = serializers.CharField(max_length=255)
    TThrdName = serializers.CharField(max_length=255)
    TDOB = serializers.DateTimeField()
    TJoinDate = serializers.DateTimeField()
    TAddress = serializers.CharField(max_length=255)
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return TeacherData.objects.create(**validated_data)

    def update(self, instance, validate_data):
        for attr, value in validate_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class ClassSerializer(serializers.Serializer):
    ClassName = serializers.CharField(max_length=255)
    StdId = serializers.PrimaryKeyRelatedField(queryset=StudentData.objects.values_list('id', flat=True))
    SubjectId = serializers.PrimaryKeyRelatedField(queryset=Subjects.objects.values_list('id', flat=True))
    TeacherId = serializers.PrimaryKeyRelatedField(queryset=TeacherData.objects.values_list('id', flat=True))
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        std_id = validated_data.pop('StdId')
        subject_id = validated_data.pop('SubjectId')
        teacher_id = validated_data.pop('TeacherId')
        term1 = StudentData.objects.get(id=std_id)
        term2 = Subjects.objects.get(id=subject_id)
        term3 = TeacherData.objects.get(id=teacher_id)
        return Class.objects.create(StdId=term1, SubjectId=term2, TeacherId=term3, **validated_data)

    def update(self, instance, validate_data):
        std_id = validate_data.pop('StdId')
        subject_id = validate_data.pop('SubjectId')
        term1 = StudentData.objects.get(id=std_id)
        term2 = Subjects.objects.get(id=subject_id)
        instance.StdId = term1
        instance.SubjectId = term2
        for attr, value in validate_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class MarksSerializer(serializers.Serializer):
    ClassId = serializers.PrimaryKeyRelatedField(queryset=Class.objects.values_list('id', flat=True))
    StdId = serializers.PrimaryKeyRelatedField(queryset=StudentData.objects.values_list('id', flat=True))
    SubjectId = serializers.PrimaryKeyRelatedField(queryset=Subjects.objects.values_list('id', flat=True))
    Mark = serializers.IntegerField()
    MarkType = serializers.PrimaryKeyRelatedField(queryset=MarkType.objects.values_list('id', flat=True))
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        std_id = validated_data.pop('StdId')
        subject_id = validated_data.pop('SubjectId')
        class_id = validated_data.pop('ClassId')
        term1 = StudentData.objects.get(id=std_id)
        term2 = Subjects.objects.get(id=subject_id)
        term3 = Class.objects.get(id=class_id)
        return Marks.objects.create(StdId=term1, SubjectId=term2, ClassId=term3, **validated_data)

    def update(self, instance, validate_data):
        std_id = validated_data.pop('StdId')
        subject_id = validated_data.pop('SubjectId')
        class_id = validated_data.pop('ClassId')
        term1 = StudentData.objects.get(id=std_id)
        term2 = Subjects.objects.get(id=subject_id)
        term3 = Class.objects.get(id=class_id)
        instance.StdId = term1
        instance.SubjectId = term2
        instance.class_id = term3
        for attr, value in validate_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance



# def encode():
#     model = SubjectModel('SubjectName: Ruby', 'Text: hjd', 4, 2)
#     model_sr = SubjectsSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
#
# def decode():
#     stream = io.BytesIO(b'{"SubjectName":"SubjectName: Ruby","Text":"Text: hjd","Duration":4,"TermId":2}')
#     data = JSONParser().parse(stream)
#     serializers = SubjectsSerializer(data=data)
#     serializers.is_valid()
#     print(serializers.validated_data)
