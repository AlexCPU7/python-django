# Generated by Django 2.1 on 2018-08-20 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20180819_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(to='books.Author', verbose_name='Автор'),
        ),
    ]