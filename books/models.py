from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Type(models.Model):
    title = models.CharField('Название', max_length=100)
    create_dt = models.DateTimeField('Дата создания', auto_now_add=True)
    update_dt = models.DateTimeField('Дата изменения', auto_now=True)

    class Meta:
        verbose_name = 'Тип книги'
        verbose_name_plural = 'Типы книг'

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField('ФИО автора', max_length=100)
    create_dt = models.DateTimeField('Дата создания', auto_now_add=True)
    update_dt = models.DateTimeField('Дата изменения', auto_now=True)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.name


class Tag(models.Model):
    title = models.CharField('Название', max_length=100)
    create_dt = models.DateTimeField('Дата создания', auto_now_add=True)
    update_dt = models.DateTimeField('Дата изменения', auto_now=True)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.title

class Book(models.Model):
    array_language = (
        (1, 'Русский'),
        (2, 'Английский'),
    )
    title = models.CharField('Название', max_length=100)
    type_id = models.ForeignKey(Type, verbose_name='Тип литературы', on_delete=models.SET_NULL, null=True)
    author = models.ManyToManyField(Author, verbose_name='Автор')
    image = models.ImageField('Изображение', upload_to='images', blank=True)
    file = models.FileField('Файл', upload_to='files', blank=True)
    desc = RichTextField('Описание', max_length=2000, blank=True)
    language = models.PositiveSmallIntegerField('Язык', choices=array_language)
    pages = models.PositiveSmallIntegerField('Колличество страниц', validators=[
        MinValueValidator(1),
        MaxValueValidator(5000)
    ])
    year = models.PositiveSmallIntegerField('Год выпуска', validators=[
        MinValueValidator(1800),
        MaxValueValidator(2150)
    ])
    tags = models.ManyToManyField(Tag, verbose_name='Теги')
    create_dt = models.DateTimeField('Дата создания', auto_now_add=True)
    update_dt = models.DateTimeField('Дата изменения', auto_now=True)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title
