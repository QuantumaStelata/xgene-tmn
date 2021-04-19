from django.contrib import admin
from .models import Players, ClanTeam
# Register your models here.

@admin.register(Players)
class PlayersAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'team')
    list_filter = ('role', 'team')
    search_fields = ('name', 'role__role_ru', 'team__name')
    fields = (('role', 'team'), 'name', 'player_id', 'battles', 'win', 'wgr', 'wn8', 'damage', 'frags')

@admin.register(ClanTeam)
class ClanTeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'color')
    search_fields = ('name',)