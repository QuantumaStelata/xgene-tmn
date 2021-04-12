from django.db import models
from apps.main.models import ClanId
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.

class ClanRole(models.Model):
    role_ru = models.CharField(verbose_name='Должность игрока', max_length=25)

    def __str__(self):
        return self.role_ru

class ClanTeam(models.Model):
    name = models.CharField(verbose_name='Название роты', max_length=20)
    color = models.CharField(verbose_name='Цвет роты', max_length=7, default='#FFFFFF')

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = 'Рота'
        verbose_name_plural = 'Роты'

class Players(models.Model):
    clan = models.ForeignKey(ClanId, on_delete = models.CASCADE)
    role = models.ForeignKey(ClanRole, blank=True, null=True, on_delete = models.CASCADE)
    team = models.ForeignKey(ClanTeam, blank=True, null=True, on_delete = models.SET_NULL)
    player_id = models.CharField(verbose_name='ID игрока', max_length=25, primary_key=True)
    name = models.CharField(verbose_name='Имя игрока', max_length=25, blank=True)
    battles = models.CharField(verbose_name='Всего боев', max_length=25, blank=True)
    wgr = models.CharField(verbose_name='WGR', max_length=25, blank=True)
    win = models.CharField(verbose_name='Процент побед', max_length=25, blank=True)
    wn8 = models.CharField(verbose_name='Wn8', max_length=25, blank=True)
    color_wn8 = models.CharField(verbose_name='Цвет Wn8', max_length=7, blank=True)
    damage = models.CharField(verbose_name='Средний дамаг', max_length=25, blank=True)
    frags = models.CharField(verbose_name='Среднее кол-во фрагов', max_length=25, blank=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Игрок клана'
        verbose_name_plural = 'Игроки клана'
        ordering = ('role_id',)


@receiver(pre_save, sender=ClanTeam)
def save_user_profile(sender, instance, **kwargs):
    instance.name = instance.name.replace(' ', '-')
