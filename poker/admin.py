from django.contrib import admin
from poker.models import game
from poker.models import player

# Register your models here.

@admin.register(game.match_POKER)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id',)

@admin.register(game.tournament_POKER)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'win_tournament',)

@admin.register(player.player_POKER)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user',)


@admin.register(game.application_POKER_tournament_no_team)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id',)
