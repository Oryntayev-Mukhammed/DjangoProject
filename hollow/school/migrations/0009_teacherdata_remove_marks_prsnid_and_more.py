# Generated by Django 4.1.5 on 2023-04-16 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0008_class_time_create_class_time_update_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255, null=True, unique=True, verbose_name='URL')),
                ('TName', models.CharField(max_length=255, verbose_name='Имя')),
                ('TScndName', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('TThrdName', models.CharField(max_length=255, verbose_name='Отчество')),
                ('TDOB', models.DateField(verbose_name='Дата рождения')),
                ('TJoinDate', models.DateField(verbose_name='Дата зачисления')),
                ('TAddress', models.CharField(max_length=255, verbose_name='Место жительства')),
                ('time_create', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True, null=True, verbose_name='Время изменения')),
            ],
            options={
                'verbose_name': 'Учитель',
                'verbose_name_plural': 'Учителя',
                'ordering': ['id'],
            },
        ),
        migrations.RemoveField(
            model_name='marks',
            name='PrsnId',
        ),
        migrations.RemoveField(
            model_name='studentdata',
            name='PrsnId',
        ),
        migrations.AddField(
            model_name='marks',
            name='ClassId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='school.class', verbose_name='Номер группы'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='marks',
            name='StudentId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='school.studentdata', verbose_name='Ученик'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentdata',
            name='StdScndName',
            field=models.CharField(default='koda', max_length=255, verbose_name='Фамилия'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentdata',
            name='StdThrdName',
            field=models.CharField(default='koda', max_length=255, verbose_name='Отчество'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='marks',
            name='MarkType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.marktype', verbose_name='Тип Задания'),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='StdDOB',
            field=models.DateField(verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='StdName',
            field=models.CharField(max_length=255, verbose_name='Имя'),
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='PersonType',
        ),
    ]
