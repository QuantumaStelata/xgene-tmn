from django.db import models
from apps.players.models import Players
# Create your models here.

class Question(models.Model):
    title = models.CharField(verbose_name='Название опроса', max_length=250)
    max_choice = models.IntegerField(verbose_name='Макс. кол-во ответов')
    answers = models.ManyToManyField('Answer', verbose_name='Ответы')
    users = models.ManyToManyField(Players, verbose_name='Отвечающие', blank=True, null=True)
    publicate = models.BooleanField(verbose_name='Пубиловать?', default=False)
    public = models.BooleanField(verbose_name='Публичный?', default=False)
    date = models.DateTimeField(verbose_name='Дата создания', auto_now=True)
    
    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

class Answer(models.Model):
    title = models.CharField(verbose_name='Вариант ответа', max_length=250)
    users = models.ManyToManyField(Players, verbose_name='Проголосовали', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
        ordering = ('-id',)