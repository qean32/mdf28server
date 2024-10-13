from django.db import models
from users.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

from unification.models.team import team,rank,cup

# ################################# ##################### #################################

class player_CS(models.Model):
    user = models.OneToOneField(User, models.CASCADE, primary_key=True, related_name='user_123')
    name = models.CharField('имя', max_length=255,null=True,blank=True)

    team = models.ForeignKey(team, models.SET_NULL, null=True,blank=True)
    position = models.ManyToManyField('position', blank=True)
    cups = models.ManyToManyField('cup',verbose_name='кубки команды', blank=True)

    matches = models.IntegerField('кол-во матчей', default=0)
    win_matches = models.IntegerField('кол-во побед матчи', default=0)
    tournament = models.IntegerField('кол-во турниров', default=0)
    win_tournament = models.IntegerField('кол-во побед турнир', default=0)
    is_recognized = models.BooleanField('признанный игрок', default=False)
    matches_in_offers = models.IntegerField('кол-во матчей в контракте', default=0)

    rank = models.ForeignKey('rank', on_delete=models.PROTECT, null=True, blank=True, default=1)
    mmr = models.IntegerField('mmr', default=0)

    class Meta:
        verbose_name = 'игрок CS'
        verbose_name_plural = 'игроки CS'

    def __str__(self):
        return f'{self.name}'


# ################################# ###################### ################################

class player_BASCKETBALL(models.Model):
    user = models.OneToOneField(User, models.CASCADE, primary_key=True, related_name='user_1234')
    name = models.CharField('имя', max_length=255,null=True,blank=True)

    team = models.ForeignKey(team, models.SET_NULL, null=True,blank=True)
    position = models.ManyToManyField('position', blank=True)
    cups = models.ManyToManyField('cup',verbose_name='кубки команды', blank=True)


    matches = models.IntegerField('кол-во матчей', default=0)
    win_matches = models.IntegerField('кол-во побед матчи', default=0)
    tournament = models.IntegerField('кол-во турниров', default=0)
    win_tournament = models.IntegerField('кол-во побед турнир', default=0)
    is_recognized = models.BooleanField('признанный игрок', default=False)
    matches_in_offers = models.IntegerField('кол-во матчей в контракте', default=0)
    number = models.IntegerField('номер', default=0, validators=[MaxValueValidator(99), MinValueValidator(0)])


    class Meta:
        verbose_name = 'игрок BASCKETBALL'
        verbose_name_plural = 'игроки BASCKETBALL'

    def __str__(self):
        return f'{self.name}'

# ################################# ################### ###################################


class player_DOTA(models.Model):
    user = models.OneToOneField(User, models.CASCADE, primary_key=True, related_name='user_1235')
    name = models.CharField('имя', max_length=255,null=True,blank=True)

    team = models.ForeignKey(team, models.SET_NULL, null=True,blank=True)
    position = models.ManyToManyField('position', blank=True)
    cups = models.ManyToManyField('cup',verbose_name='кубки команды', blank=True)

    matches = models.IntegerField('кол-во матчей', default=0)
    win_matches = models.IntegerField('кол-во побед матчи', default=0)
    tournament = models.IntegerField('кол-во турниров', default=0)
    win_tournament = models.IntegerField('кол-во побед турнир', default=0)
    is_recognized = models.BooleanField('признанный игрок', default=False)
    matches_in_offers = models.IntegerField('кол-во матчей в контракте', default=0)

    rank = models.ForeignKey('rank', on_delete=models.PROTECT, null=True, blank=True, default=1)
    mmr = models.IntegerField('mmr', default=0)

    class Meta:
        verbose_name = 'игрок DOTA'
        verbose_name_plural = 'игроки DOTA'

    def __str__(self):
        return f'{self.name}'

# ################################# ################### ###################################

class position(models.Model):
    name = models.CharField('позиция', max_length=55)
    image = models.ImageField('лого команды', blank=True, null=True, upload_to='team/position/')

    class Meta:
        verbose_name = 'позиция'
        verbose_name_plural = 'позиции'
    def __str__(self):
        return f'{self.name}, {self.pk}'