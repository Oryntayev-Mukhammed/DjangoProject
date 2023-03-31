# Generated by Django 4.1.5 on 2023-03-08 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_alter_class_options_alter_marks_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='SubjectId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='school.subjects', verbose_name='Занятие'),
            preserve_default=False,
        ),
    ]