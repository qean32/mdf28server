from django.db import models
from users.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from b_unification.models.team import team
from direction.models import direction

# Create your models here.

class meeting(models.Model):
    team_one = models.ForeignKey(team, models.SET_NULL, null=True, blank=True, related_name='team_meeting_one')
    team_two = models.ForeignKey(team, models.SET_NULL, null=True, blank=True, related_name='team_meeting_two')
    win_team = models.ForeignKey(team, models.SET_NULL, null=True, blank=True, related_name='team_meeting_win')

    is_friends = models.BooleanField('дружеский', default=True)
    is_qualification = models.BooleanField('квалификация', default=False)

    team_one_score = models.IntegerField('счет команды один',  null=True,blank=True, default=0)
    team_two_score = models.IntegerField('счет команды два', null=True,blank=True, default=0)
    
    team_one_ball = models.IntegerField('баллы команды один',  null=True,blank=True, default=0)
    team_two_ball = models.IntegerField('баллы команды два', null=True,blank=True, default=0)

    date = models.DateField('датa', null=True, blank=True)
    created_at = models.DateTimeField('дата', default=timezone.now)

    tournament = models.ForeignKey('tournament', models.SET_NULL , null=True, blank=True)
    matches = models.IntegerField('b0', validators=[MaxValueValidator(3), MinValueValidator(0)], default=2)
    direction = models.ForeignKey(direction,  on_delete=models.SET_NULL, null=True, blank=True,related_name='dir124ec123tion21_12')

    class Meta:
        verbose_name = 'встреча'
        verbose_name_plural = 'встречи'

    def __str__(self):
        return f'{self.team_one}, {self.team_two}'
        
# ################################# ############# #########################################  

class match(models.Model):
    team_one = models.ForeignKey(team, models.SET_NULL, null=True, blank=True, related_name='team_match_one')
    team_two = models.ForeignKey(team, models.SET_NULL, null=True, blank=True, related_name='team_match_two')
    win_team = models.ForeignKey(team, models.SET_NULL, null=True, blank=True, related_name='team_match_win')

    time = models.TimeField('время начала',default='20:00')
    created_at = models.DateTimeField('дата', default=timezone.now)
    date = models.DateField('датa', null=True, blank=True)

    team_one_score = models.IntegerField('счет команды один',  null=True,blank=True, default=0)
    team_two_score = models.IntegerField('счет команды два', null=True,blank=True, default=0)

    id_match = models.IntegerField('ид матча', default=0)
    meeting = models.ForeignKey(meeting, models.SET_NULL ,null=True,blank=True)
    direction = models.ForeignKey(direction,  on_delete=models.SET_NULL, null=True, blank=True,related_name='dir124ec12123tion21_12')

    class Meta:
        verbose_name = 'матч'
        verbose_name_plural = 'матчи'

    def __str__(self):
        return f'{self.team_one}, {self.team_two}'
        
# ################################# ############# #########################################  

class tournament(models.Model):
    name = models.CharField('название', max_length=255, blank=True, null=True)
    about = models.CharField('описание', max_length=255, blank=True, null=True)

    win_tournament = models.ForeignKey(team,models.SET_NULL, null=True, blank=True, related_name='team_DOTA_w12in_tournament')
    teams = models.ManyToManyField(team, 'team_DOTA_play', verbose_name='команды-участники', blank=True)

    created_at = models.DateTimeField('дата', default=timezone.now)
    date = models.DateField('датa', null=True, blank=True)
    is_on = models.BooleanField('закрыт',default=False)
    price_tournament = models.IntegerField('призовой фонд', null=True, blank=True)
    direction = models.ForeignKey(direction,  on_delete=models.SET_NULL, null=True, blank=True,related_name='dir124ec123tion21_1fsg2')

    class Meta:
        verbose_name = 'турнир'
        verbose_name_plural = 'турниры'

    def __str__(self):
        return f'{self.name}'

# ################################# ############# #########################################  

class application_tournament(models.Model):
    created_at = models.DateTimeField('дата', default=timezone.now)
    team = models.ForeignKey(team, models.SET_NULL, null=True, blank=True, related_name='team_applicat412ion_tournament')
    tournament = models.ForeignKey(tournament,models.SET_NULL, null=True, blank=True, related_name='tournament_a123pplication_tournament')
    direction = models.ForeignKey(direction,  on_delete=models.SET_NULL, null=True, blank=True,related_name='dir124ec123dastion21_12')
    is_on = models.BooleanField('одобренно', default=False)

    class Meta:
        verbose_name = 'заявка на турнир'
        verbose_name_plural = 'заявки на турниры'

    def __str__(self):
        return f'{self.team}'


class application_meeting(models.Model):
    created_at = models.DateTimeField('дата', default=timezone.now)
    date = models.DateField('дата',null=True,blank=True)
    
    team_one = models.ForeignKey(team, models.SET_NULL, null=True, blank=True, related_name='team_142z4xcc')
    team_two = models.ForeignKey(team, models.SET_NULL, null=True, blank=True, related_name='tea123m_ztwo') 
    direction = models.ForeignKey(direction,  on_delete=models.SET_NULL, null=True, blank=True,related_name='dir124ec123tion21_wqsemasd12')

    is_accept = models.BooleanField('одобренно командой', default=False)
    is_on = models.BooleanField('одобренно', default=False)

    matches = models.IntegerField('b0', validators=[MaxValueValidator(3), MinValueValidator(0)], default=2)
    time1 = models.TimeField('время начала',default='18:00')
    time2 = models.TimeField('время начала',default='18:00')

    class Meta:
        verbose_name = 'вызов на матчи'
        verbose_name_plural = 'вызовы на матчи'

    def __str__(self):
        return f'{self.team_one}, {self.team_two}'

# ################################# ############# #########################################    