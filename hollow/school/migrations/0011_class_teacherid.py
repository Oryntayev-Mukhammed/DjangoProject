# Generated by Django 4.1.5 on 2023-04-23 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0010_alter_class_time_create_alter_class_time_update_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='TeacherId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='school.teacherdata', verbose_name='Учитель'),
            preserve_default=False,
        ),
    ]
