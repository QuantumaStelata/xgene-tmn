from django.db import models

# Create your models here.

class ClanId(models.Model):
    clan_id = models.CharField(verbose_name="ID клана", max_length=6)

    def __str__(self):
        return self.clan_id

    class Meta:
        verbose_name = 'ID клана'
        verbose_name_plural = 'ID клана'

class ClanInfo(models.Model):
    tag = models.CharField(verbose_name='Тэг клана', max_length=5, primary_key=True)
    name = models.CharField(verbose_name='Название клана', max_length=25, blank=True)
    motto = models.CharField(verbose_name='Девиз клана', max_length=100, blank=True)
    color = models.CharField(verbose_name='Цвет клана', max_length=7, blank=True)
    emblem = models.CharField(verbose_name='Эмблема клана', max_length=300, blank=True)
    
    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = 'Информация о клане'
        verbose_name_plural = 'Информация о клане'

class ClanStatistic(models.Model):
    sh10 = models.CharField(verbose_name='Эло укрепрайона X', max_length=4, blank=True)
    sh8 = models.CharField(verbose_name='Эло укрепрайона VIII', max_length=4, blank=True)
    sh6 = models.CharField(verbose_name='Эло укрепрайона VI', max_length=4, blank=True)
    gm10 = models.CharField(verbose_name='Эло глобальной карты X', max_length=4, blank=True)
    gm8 = models.CharField(verbose_name='Эло глобальной карты VIII', max_length=4, blank=True)
    gm6 = models.CharField(verbose_name='Эло глобальной карты VI', max_length=4, blank=True)
    battles_count = models.CharField(verbose_name='Среднее кол-во боев', max_length=10, blank=True)
    win_rate = models.CharField(verbose_name='Среднее процент побед', max_length=10, blank=True)
    rate = models.CharField(verbose_name='Рейтинг клана', max_length=10, blank=True)
    position = models.CharField(verbose_name='Позиция клана', max_length=10, blank=True)
    xp_per_battle = models.CharField(verbose_name='Средний опыт за бой', max_length=10, blank=True)
    damage_per_battle = models.CharField(verbose_name='Средний урон за бой', max_length=10, blank=True)
    static_update = models.DateTimeField(verbose_name='Время обновления статистики', auto_now=True)

    def __str__(self):
        return self.position

    class Meta:
        verbose_name = 'Статистика клана'
        verbose_name_plural = 'Статистика клана'

