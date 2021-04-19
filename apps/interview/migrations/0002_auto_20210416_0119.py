# Generated by Django 3.1.6 on 2021-04-15 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0008_auto_20210410_0419'),
        ('interview', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'ordering': ('-id',), 'verbose_name': 'Ответ', 'verbose_name_plural': 'Ответы'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Опрос', 'verbose_name_plural': 'Опросы'},
        ),
        migrations.AddField(
            model_name='answer',
            name='users',
            field=models.ManyToManyField(to='players.Players', verbose_name='Проголосовали'),
        ),
    ]