# Generated by Django 3.1.6 on 2021-04-15 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Вариант ответа')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название опроса')),
                ('publicate', models.BooleanField(default=False, verbose_name='Пубиловать?')),
                ('max_choice', models.IntegerField(verbose_name='Макс. кол-во ответов')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
                ('answers', models.ManyToManyField(to='interview.Answer', verbose_name='Ответы')),
            ],
        ),
    ]
