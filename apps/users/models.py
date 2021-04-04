from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.players.models import Players
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    player = models.OneToOneField(Players, blank=True, null=True, on_delete=models.CASCADE)
    token = models.CharField(verbose_name='Токен', blank=True, max_length=400)
    # image = models.ImageField(verbose_name='Фото игрока', blank=True)
    photo = models.CharField(verbose_name='Фото игрока', blank=True, max_length=300)
    streamer = models.BooleanField(verbose_name='Стример', default=False)
    url = models.CharField(verbose_name='Ссылка на канал', blank=True, max_length=300)

    def __str__(self):
        return self.user.username

    class Meta():
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()