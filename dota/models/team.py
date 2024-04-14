from django.db import models
from users.models import User
from django.utils import timezone

from colorfield.fields import ColorField
from generation.models import generation

# ################################# ##################### #################################

class team_DOTA(models.Model):
    team_name = models.CharField('название команды', max_length=30, default='clown`s', unique=True)
    logo = models.ImageField('лого команды', blank=True, null=True, upload_to='team_DOTA/logo/')
    background = models.ImageField('фон', blank=True, null=True, upload_to='team_DOTA/background/')
    status = models.CharField('статус', max_length=255, null=True, blank=True)
    detail = models.CharField('подробно', max_length=255, null=True, blank=True)
    director = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    date_crate = models.DateTimeField('дата создания', default=timezone.now)
    cups = models.ManyToManyField('cup_DOTA',verbose_name='кубки команды', blank=True)
    matches = models.IntegerField('кол-во матчей', default=0)
    win_matches = models.IntegerField('кол-во побед матчи', default=0)
    tournament = models.IntegerField('кол-во турниров', default=0)
    win_tournament = models.IntegerField('кол-во побед турнир', default=0)
    is_recognized = models.BooleanField('признанный игрок', default=False)
    color = ColorField('цвет',default='#3749FF')
    
    kill = models.IntegerField('убийства', default=0)
    death = models.IntegerField('смерти', default=0)
    assist = models.IntegerField('ассисты', default=0)

    class Meta:
        verbose_name = 'команда'
        verbose_name_plural = 'команды'

    def __str__(self):
        return f'{self.team_name}, {self.pk}'


# ################################# ###################### ################################


class player_DOTA(models.Model):
    user = models.OneToOneField(User, models.CASCADE, primary_key=True)
    name = models.CharField('имя', max_length=30,null=True,blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    # ################################# #################### ##################################

    team = models.ForeignKey(team_DOTA, models.SET_NULL, null=True,blank=True)
    generation = models.ForeignKey(generation, models.SET_NULL, null=True, blank=True)
    position = models.ManyToManyField('position_DOTA', blank=True)
    cups = models.ManyToManyField('solo_cup_DOTA',verbose_name='кубки команды', blank=True)

    # ################################# ################# #####################################

    matches = models.IntegerField('кол-во матчей', default=0)
    win_matches = models.IntegerField('кол-во побед матчи', default=0)
    tournament = models.IntegerField('кол-во турниров', default=0)
    win_tournament = models.IntegerField('кол-во побед турнир', default=0)
    is_recognized = models.BooleanField('признанный игрок', default=False)
    matches_in_offers = models.IntegerField('кол-во матчей в контракте', default=0)

    # ################################# ################# #####################################

    rank = models.ForeignKey('rank_DOTA', on_delete=models.PROTECT, null=True, blank=True, default=1)
    pts = models.IntegerField('птс', default=0)
    nickname = models.CharField('никнейм_DOTA', max_length=55, blank=True, null=True)

    class Meta:
        verbose_name = 'игрок'
        verbose_name_plural = 'игроки'

    def __str__(self):
        return f'{self.user}'

    # ################################# ################### ###################################


class offers_DOTA(models.Model):
    is_view = models.BooleanField('согласие пользователя', default=False)
    user = models.ForeignKey(User, models.CASCADE)
    team = models.ForeignKey(team_DOTA, on_delete=models.CASCADE)
    generation = models.ForeignKey(generation, models.SET_NULL, null=True)
    position = models.ManyToManyField('position_DOTA', blank=True)
    date = models.DateTimeField('дата', default=timezone.now)
    matches_in_offers = models.IntegerField('кол-во матчей в контракте', default=1)


    class Meta:
        verbose_name = 'оффер'
        verbose_name_plural = 'офферы'

    def __str__(self):
        return f'оффер {self.pk}'

    # ################################# ################## ####################################


class rank_DOTA(models.Model):
    rank_name = models.CharField('ранг', max_length=55)
    image_rank = models.ImageField('картинка ранга', blank=True, null=True, upload_to='rank_DOTA/')

    class Meta:
        verbose_name = 'ранг'
        verbose_name_plural = 'ранги'
    def __str__(self):
        return f'{self.rank_name}, {self.pk}'


class position_DOTA(models.Model):
    position_name = models.CharField('позиция', max_length=55)
    image_position = models.ImageField('картинка позиции', blank=True, null=True, upload_to='position_DOTA/')

    class Meta:
        verbose_name = 'позиция'
        verbose_name_plural = 'позиции'
    def __str__(self):
        return f'{self.position_name}, {self.pk}'

 # ################################# ############# #########################################

class cup_DOTA(models.Model):
    name = models.CharField('название', max_length=30,null=True,blank=True)
    image = models.ImageField('лого кубка', blank=True, null=True, upload_to='cup/dota/')

    class Meta:
        verbose_name = 'кубок_комады'
        verbose_name_plural = 'кубки_команды'

    def __str__(self):
        return f'{self.name}'

class solo_cup_DOTA(models.Model):
    name = models.CharField('название', max_length=30,null=True,blank=True)
    image = models.ImageField('лого кубка', blank=True, null=True, upload_to='cup_solo/dota/')

    class Meta:
        verbose_name = 'кубок_соло'
        verbose_name_plural = 'кубки_соло'

    def __str__(self):
        return f'{self.name}'