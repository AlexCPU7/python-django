# Generated by Django 2.1 on 2018-08-19 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20180815_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='link',
            field=models.CharField(blank=True, max_length=400, verbose_name='Ссылка/источник'),
        ),
    ]
