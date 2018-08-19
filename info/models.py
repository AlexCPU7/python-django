from django.db import models
from ckeditor.fields import RichTextField


class Content(models.Model):
    title = models.CharField('Название', max_length=100)
    text = RichTextField('Текст')

    class Meta:
        verbose_name = 'Контент'
        verbose_name_plural = 'Контенты'

    def __str__(self):
        return self.title