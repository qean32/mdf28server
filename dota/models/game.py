from django.db import models
from users.models import User
from django.utils import timezone
from dota.models.team import team_DOTA,player_DOTA
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class meeting_DOTA(models.Model):
    team_one = models.ForeignKey(team_DOTA, models.SET_NULL, null=True, blank=True, related_name='team_DOTA_one')
    team_two = models.ForeignKey(team_DOTA, models.SET_NULL, null=True, blank=True, related_name='team_DOTA_two')
    is_friends = models.BooleanField('дружеский', default=True)
    created_at = models.DateTimeField('дата', default=timezone.now)
    win_team = models.ForeignKey(team_DOTA, models.SET_NULL, null=True, blank=True, related_name='team_DOTA_win')
    team_one_score = models.IntegerField('счет команды один',  null=True,blank=True, default=0)
    team_two_score = models.IntegerField('счет команды два', null=True,blank=True, default=0)
    is_qualification = models.BooleanField('квалификация', default=False)
    team_one_ball = models.IntegerField('баллы команды один',  null=True,blank=True, default=0)
    team_two_ball = models.IntegerField('баллы команды два', null=True,blank=True, default=0)
    date = models.DateField('датa', null=True, blank=True)
    teams_structure_one = models.ManyToManyField(player_DOTA, 'team_DOTA_play_srtucture_1_DOTA', verbose_name='состав команды 1', blank=True)
    teams_structure_two = models.ManyToManyField(player_DOTA, 'team_DOTA_play_srtucture_2_DOTA', verbose_name='состав команды 2', blank=True)
    tournament = models.ForeignKey('tournament_DOTA', models.SET_NULL , null=True, blank=True)
    matches = models.IntegerField('b0', validators=[MaxValueValidator(3)], default=2)

    class Meta:
        verbose_name = 'встреча'
        verbose_name_plural = 'встречи'
    def __str__(self):
        return f'{self.team_one}, {self.team_two}'

class match_DOTA(models.Model):
    team_one = models.ForeignKey(team_DOTA, models.SET_NULL, null=True, blank=True, related_name='teame12_DOTA_one')
    team_two = models.ForeignKey(team_DOTA, models.SET_NULL, null=True, blank=True, related_name='teamqes_DOTA_two')
    created_at = models.DateTimeField('дата', default=timezone.now)
    win_team = models.ForeignKey(team_DOTA, models.SET_NULL, null=True, blank=True, related_name='team_DOTe12qA_win')
    team_one_score = models.IntegerField('счет команды один',  null=True,blank=True, default=0)
    team_two_score = models.IntegerField('счет команды два', null=True,blank=True, default=0)
    id_match = models.IntegerField('ид матча', default=0)
    time = models.TimeField('время начала',default='20:00')
    meeting = models.ForeignKey(meeting_DOTA, models.SET_NULL ,null=True,blank=True)

    class Meta:
        verbose_name = 'матч'
        verbose_name_plural = 'матчи'
    def __str__(self):
        return f'{self.team_one}, {self.team_two}'

class tournament_DOTA(models.Model):
    name = models.CharField('название турнира', max_length=255, blank=True, null=True)
    teams = models.ManyToManyField(team_DOTA, 'team_DOTA_play', verbose_name='команды-участники', blank=True)
    created_at = models.DateTimeField('дата', default=timezone.now)
    win_tournament = models.ForeignKey(team_DOTA,models.SET_NULL, null=True, blank=True, related_name='team_DOTA_win_tournament')
    price_tournament = models.IntegerField('призовой фонд', null=True, blank=True)
    date = models.DateField('датa', null=True, blank=True)
    is_on = models.BooleanField('открыт',default=False)

    class Meta:
        verbose_name = 'турнир'
        verbose_name_plural = 'турниры'
    def __str__(self):
        return f'{self.name}'

class application_DOTA_tournament(models.Model):
    date = models.DateTimeField('дата', default=timezone.now)
    author = models.ForeignKey(User, models.SET_NULL, null=True, blank=True, related_name='director_zxcc')
    team = models.ForeignKey(team_DOTA, models.SET_NULL, null=True, blank=True, related_name='team_zxcc')
    is_on = models.BooleanField('одобренно', default=False)
    tournament = models.ForeignKey(tournament_DOTA,models.SET_NULL, null=True, blank=True, related_name='fsdeafsa')

    class Meta:
        verbose_name = 'заявки на турниры'
        verbose_name_plural = 'заявки на турниры'
    def __str__(self):
        return f'{self.team}'


class application_DOTA_meeting(models.Model):
    created_at = models.DateTimeField('дата', default=timezone.now)
    date = models.DateField('дата',null=True,blank=True)
    author = models.ForeignKey(User, models.SET_NULL, null=True, blank=True, related_name='director_z1xcc')
    team_one = models.ForeignKey(team_DOTA, models.SET_NULL, null=True, blank=True, related_name='team_z4xcc')
    team_two = models.ForeignKey(team_DOTA, models.SET_NULL, null=True, blank=True, related_name='team_ztwo')
    is_accept = models.BooleanField('одобренно командой', default=False)
    is_on = models.BooleanField('одобренно', default=False)
    matches = models.IntegerField('b0', validators=[MaxValueValidator(3)], default=2)
    time1 = models.TimeField('время начала',default='18:00')
    time2 = models.TimeField('время начала',default='18:00')

    class Meta:
        verbose_name = 'вызов на матчи'
        verbose_name_plural = 'вызовы на матчи'

    def __str__(self):
        return f'{self.team_one}, {self.team_two}'



# ################################# ############# #########################################        
        
class record_stat(models.Model):
    user = models.ForeignKey(User, models.CASCADE, related_name='teame1BASCKETBAL123Le_DOTA_onedwsads')
    match = models.ForeignKey(match_DOTA, models.SET_NULL,null=True, related_name='teameqdw1BASCKETBALLe_DOTA_onesdqw')
    
    kill = models.IntegerField('убийства', default=0)
    death = models.IntegerField('смерти', default=0)
    assist = models.IntegerField('ассисты', default=0)
    damage = models.IntegerField('урон', default=0)
    win = models.BooleanField('победа', default=False)
    heal = models.IntegerField('хил', default=0)
    damage_t = models.IntegerField('урон башням', default=0)
    hero = models.ForeignKey('hero', models.SET_NULL, null=True, related_name='teameqdw1BASCKETBALLe_DOTA_onesdqw12')
    first_team = models.BooleanField('1 тим', default=False)
    gold = models.IntegerField('золото', default=0)

    class Meta:
        verbose_name = 'статистика игрока'
        verbose_name_plural = 'статистики игроков'

    def str(self):
        return f'{self.user}'

class hero(models.Model):
    hero_name = models.CharField('имя героя', default='clown`s', unique=True,max_length=45)
    hero_image = models.ImageField('картинка героя', blank=True, null=True, upload_to='dota/hero/')

    class Meta:
        verbose_name = 'герой'
        verbose_name_plural = 'герои'

    def str(self):
        return f'{self.hero_name}'