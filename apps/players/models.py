from django.db import models
from apps.main.models import ClanId

# Create your models here.

class ClanRole(models.Model):
    role_ru = models.CharField(verbose_name='Должность игрока', max_length=25)

    def __str__(self):
        return self.role_ru

class Players(models.Model):
    clan = models.ForeignKey(ClanId, on_delete = models.CASCADE)
    role = models.ForeignKey(ClanRole, on_delete = models.CASCADE)
    player_id = models.CharField(verbose_name='ID игрока', max_length=25, primary_key=True)
    name = models.CharField(verbose_name='Имя игрока', max_length=25)
    battles = models.CharField(verbose_name='Всего боев', max_length=25, blank=True)
    wgr = models.CharField(verbose_name='WGR', max_length=25, blank=True)
    win = models.CharField(verbose_name='Процент побед', max_length=25, blank=True)
    damage = models.CharField(verbose_name='Средний дамаг', max_length=25, blank=True)
    frags = models.CharField(verbose_name='Среднее кол-во фрагов', max_length=25, blank=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Игрок клана'
        verbose_name_plural = 'Игроки клана'
        ordering = ('role_id',)