from django.contrib import admin

from unification.models import game
from unification.models import team


@admin.register(game.match)
class UserAdmin(admin.ModelAdmin):
    list_display = ('team_one','team_two',)

@admin.register(game.meeting)
class UserAdmin(admin.ModelAdmin):
    list_display = ('team_one','team_two',)

@admin.register(game.tournament)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(team.team)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(team.cup)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(team.offers)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'team',)
#
@admin.register(team.rank)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(game.application_tournament)
class UserAdmin(admin.ModelAdmin):
    list_display = ('is_on',)

@admin.register(team.player)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user',)