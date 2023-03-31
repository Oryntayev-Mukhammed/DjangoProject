# Generated by Django 4.1.5 on 2023-02-12 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ClassName', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Mark', models.IntegerField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MarkType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MarkType', models.CharField(max_length=255)),
                ('TypeName', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PrsnFristName', models.CharField(max_length=255)),
                ('PrsnScndName', models.CharField(max_length=255)),
                ('PrsnThrdName', models.CharField(max_length=255)),
                ('PrsnDOB', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PersonType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Prsntype', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='StudentData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StdName', models.CharField(max_length=255)),
                ('StdDOB', models.CharField(max_length=255)),
                ('StdJoinDate', models.DateField()),
                ('StdAddress', models.CharField(max_length=255)),
                ('PrsnId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.person')),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SubjectName', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Terms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TermName', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='MariType',
        ),
        migrations.AddField(
            model_name='subjects',
            name='TermId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.terms'),
        ),
        migrations.AddField(
            model_name='person',
            name='PrsnType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.persontype'),
        ),
        migrations.AddField(
            model_name='marks',
            name='MarkType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.marktype'),
        ),
        migrations.AddField(
            model_name='marks',
            name='PrsnId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.person'),
        ),
        migrations.AddField(
            model_name='marks',
            name='SubjectId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.subjects'),
        ),
        migrations.AddField(
            model_name='class',
            name='StdId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.studentdata'),
        ),
    ]