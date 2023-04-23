# Generated by Django 4.1.5 on 2023-04-23 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0009_teacherdata_remove_marks_prsnid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='class',
            name='time_update',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Время изменения'),
        ),
        migrations.AlterField(
            model_name='marks',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='marks',
            name='time_update',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Время изменения'),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='StdAddress',
            field=models.CharField(default='koda', max_length=255, verbose_name='Место жительства'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='StdDOB',
            field=models.DateField(default='2023-04-23', verbose_name='Дата рождения'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='StdJoinDate',
            field=models.DateField(default='2023-04-23', verbose_name='Дата зачисления'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='StdName',
            field=models.CharField(default='koda', max_length=255, verbose_name='Имя'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='StdScndName',
            field=models.CharField(default='koda', max_length=255, verbose_name='Фамилия'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='StdThrdName',
            field=models.CharField(default='koda', max_length=255, verbose_name='Отчество'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teacherdata',
            name='TAddress',
            field=models.CharField(default='koda', max_length=255, verbose_name='Место жительства'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teacherdata',
            name='TDOB',
            field=models.DateField(default='2023-04-23', verbose_name='Дата рождения'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teacherdata',
            name='TJoinDate',
            field=models.DateField(default='2023-04-23', verbose_name='Дата зачисления'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teacherdata',
            name='TName',
            field=models.CharField(default='Koda', max_length=255, verbose_name='Имя'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teacherdata',
            name='TScndName',
            field=models.CharField(default='koda', max_length=255, verbose_name='Фамилия'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teacherdata',
            name='TThrdName',
            field=models.CharField(default='koda', max_length=255, verbose_name='Отчество'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teacherdata',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='teacherdata',
            name='time_update',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Время изменения'),
        ),
    ]