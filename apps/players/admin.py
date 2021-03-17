from django.contrib import admin
from .models import Players
# Register your models here.

@admin.register(Players)
class PlayersAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')
    list_filter = ('role',)
    search_fields = ('name', 'role__role_ru')
    fields = ('role', 'name', 'player_id', 'battles', 'win', 'wgr', 'damage', 'frags')