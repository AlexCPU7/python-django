# Generated by Django 2.1 on 2018-08-15 16:21

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ФИО автора')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update_dt', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('image', models.ImageField(blank=True, upload_to='images', verbose_name='Изображение')),
                ('file', models.FileField(blank=True, upload_to='files', verbose_name='Файл')),
                ('desc', ckeditor.fields.RichTextField(blank=True, max_length=2000, verbose_name='Описание')),
                ('language', models.PositiveSmallIntegerField(choices=[(1, 'Русский'), (2, 'Английский')], verbose_name='Язык')),
                ('pages', models.PositiveSmallIntegerField(verbose_name='Колличество страниц')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update_dt', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('author', models.ManyToManyField(to='books.Author', verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update_dt', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update_dt', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
            ],
            options={
                'verbose_name': 'Тип книги',
                'verbose_name_plural': 'Типы книг',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='tags',
            field=models.ManyToManyField(to='books.Tag', verbose_name='Теги'),
        ),
        migrations.AddField(
            model_name='book',
            name='type_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='books.Type', verbose_name='Тип литературы'),
        ),
    ]
