from django.contrib import admin

# Register your models here.
from .models import ClanId, ClanStatistic, ClanInfo


@admin.register(ClanId)
class ClanIdAdmin(admin.ModelAdmin):
    list_display = ('clan_id',)

@admin.register(ClanInfo)
class ClanInfoAdmin(admin.ModelAdmin):
    list_display = ('tag',)
    fields = ('color',)

@admin.register(ClanStatistic)
class ClanStatisticAdmin(admin.ModelAdmin):
    list_display = ('static_update',)
    fields = (('sh10', 'sh8', 'sh6'), ('gm10', 'gm8', 'gm6'), ('battles_count', 'win_rate'), ('rate', 'position'), ('xp_per_battle', 'damage_per_battle'))
