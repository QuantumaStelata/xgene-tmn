# Generated by Django 3.1.6 on 2021-04-01 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='nick',
            field=models.CharField(max_length=100, verbose_name='Ник автора'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.CharField(max_length=300, verbose_name='Текст комментария'),
        ),
    ]