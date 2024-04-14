from django.contrib import admin
from cs.models import game
from cs.models import team

# Register your models here.

@admin.register(game.record_stat)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'match',)

@admin.register(game.match_CS)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','team_one','team_two',)

@admin.register(game.meeting_CS)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','team_one','team_two',)

@admin.register(game.tournament_CS)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)

@admin.register(team.team_CS)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'team_name',)

@admin.register(team.player_CS)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user',)

@admin.register(team.cup_CS)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(team.solo_cup_CS)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(team.offers_CS)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'team',)
#
@admin.register(team.rank_CS)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'rank_name',)

@admin.register(team.position_CS)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'position_name',)

@admin.register(game.application_CS_tournament)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id',)

@admin.register(game.application_CS_meeting)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id',)

