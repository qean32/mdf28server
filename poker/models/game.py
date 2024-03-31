from django.db import models
from users.models import User
from django.utils import timezone
from poker.models.player import player_POKER
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class match_POKER(models.Model):
    id = models.BigAutoField(primary_key=True)
    win = models.ForeignKey(player_POKER, models.SET_NULL, null=True, blank=True, related_name='player_POKER_win')
    player = models.ManyToManyField(player_POKER, 'team_POKER_play', verbose_name='участники', blank=True)

    data = models.DateField('датa', null=True, blank=True)
    time_hour = models.IntegerField('время начала в часах', default=0, validators=[MaxValueValidator(23)])
    time_minutes = models.IntegerField('время начала в минутах', default=0, validators=[MaxValueValidator(59)])
    org = models.ForeignKey(User, models.SET_NULL, null=True, blank=True, related_name='organisation_match_POKER')
    price_match = models.IntegerField('призовой фонд', null=True,default=0)

    class Meta:
        verbose_name = 'матч_POKER'
        verbose_name_plural = 'матчи_POKER'
    def __str__(self):
        return f'{self.id}'

class tournament_POKER(models.Model):

    name = models.CharField('название турнира', max_length=255, blank=True, null=True)
    player = models.ManyToManyField(player_POKER, 'team_POKER_playy', verbose_name='участники', blank=True)

    matches = models.ManyToManyField(match_POKER,verbose_name='матчи турнира', blank=True)
    win_tournament = models.ForeignKey(player_POKER,models.SET_NULL, null=True, blank=True, related_name='POKER_win_tournament')
    price_tournament = models.IntegerField('призовой фонд', null=True,default=0)

    data = models.DateField('датa', null=True, blank=True)
    time_hour = models.IntegerField('время начала в часах', default=0, validators=[MaxValueValidator(23)])
    time_minutes = models.IntegerField('время начала в минутах', default=0, validators=[MaxValueValidator(59)])
    org = models.ForeignKey(User, models.SET_NULL, null=True, blank=True, related_name='organisation_tournament_POKER')

    class Meta:
        verbose_name = 'турнир_POKER'
        verbose_name_plural = 'турниры_POKER'
    def __str__(self):
        return f'{self.id}'

class application_POKER_tournament_no_team(models.Model):

    date = models.DateField('дата', default=timezone.now)

    author = models.ForeignKey(User, models.SET_NULL, null=True, blank=True, related_name='dire2ctor_zx3cc')
    is_on = models.BooleanField('одобренно', default=False)

    class Meta:
        verbose_name = 'заявки на турниры'
        verbose_name_plural = 'тзаявки на турниры'
    def __str__(self):
        return f'{self.id}'