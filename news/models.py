from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField

User = get_user_model()

# Create your models here.

class Category(models.Model):
    title = models.CharField('Заголовок', max_length=50)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField('Заголовок', max_length=50)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.title

class News(models.Model):
    user = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)        #при удалении user строка не удалится
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True)
    title = models.CharField('Заголовок', max_length=100)
    text_anons = RichTextField('Текст (анонс)', max_length=350)
    text = RichTextField('Текст статьи')
    tags = models.ManyToManyField(Tag, verbose_name='Теги')
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    descr = models.CharField('Описание', max_length=100)
    keywords = models.CharField('Ключевые слова', max_length=50)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        #return self.title
        return 'Автор %s название %s'%(self.user, self.title)

