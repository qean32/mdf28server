from django.db import models
from users.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

from colorfield.fields import ColorField

# ################################# ##################### #################################

class team_BASCKETBALL(models.Model):
    team_name = models.CharField('название команды', max_length=30, default='clown`s', unique=True)
    logo = models.ImageField('лого команды', blank=True, null=True, upload_to='team_BASCKETBALL/logo/')
    background = models.ImageField('фон', blank=True, null=True, upload_to='team_BASCKETBALL/background/')
    status = models.CharField('статус', max_length=255, null=True, blank=True)
    detail = models.CharField('подробно', max_length=255, null=True, blank=True)
    director = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    date_crate = models.DateTimeField('дата создания', default=timezone.now)
    cups = models.ManyToManyField('cup_BASCKETBALL',verbose_name='кубки команды', blank=True)
    matches = models.IntegerField('кол-во матчей', default=0)
    win_matches = models.IntegerField('кол-во побед матчи', default=0)
    tournament = models.IntegerField('кол-во турниров', default=0)
    win_tournament = models.IntegerField('кол-во побед турнир', default=0)
    is_recognized = models.BooleanField('признанный игрок', default=False)
    color = ColorField('цвет',default='#3749FF')

    class Meta:
        verbose_name = 'команда'
        verbose_name_plural = 'команды'

    def __str__(self):
        return f'{self.team_name}, {self.pk}'


# ################################# ###################### ################################


class player_BASCKETBALL(models.Model):
    user = models.OneToOneField(User, models.CASCADE, primary_key=True)
    name = models.CharField('имя', max_length=30,null=True,blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    # ################################# #################### ##################################

    team = models.ForeignKey(team_BASCKETBALL, models.SET_NULL, null=True,blank=True)
    generation = models.ForeignKey('generation_BASCKETBALL', models.SET_NULL, null=True, blank=True)
    position = models.ManyToManyField('position_BASCKETBALL', blank=True)
    cups = models.ManyToManyField('solo_cup_BASCKETBALL',verbose_name='кубки команды', blank=True)

    # ################################# ################# #####################################

    matches = models.IntegerField('кол-во матчей', default=0)
    win_matches = models.IntegerField('кол-во побед матчи', default=0)
    tournament = models.IntegerField('кол-во турниров', default=0)
    win_tournament = models.IntegerField('кол-во побед турнир', default=0)
    is_recognized = models.BooleanField('признанный игрок', default=False)
    matches_in_offers = models.IntegerField('кол-во матчей в контракте', default=0)

    # ################################# ################# #####################################

    number = models.IntegerField('номер', default=1, validators=[MaxValueValidator(99)] )
    translit = models.CharField('никнейм_BASCKETBALL', max_length=55, blank=True, null=True)

    class Meta:
        verbose_name = 'игрок'
        verbose_name_plural = 'игроки'

    def __str__(self):
        return f'{self.user}'

    # ################################# ################### ###################################


class offers_BASCKETBALL(models.Model):
    is_view = models.BooleanField('согласие пользователя', default=False)
    user = models.ForeignKey(User, models.CASCADE)
    team = models.ForeignKey(team_BASCKETBALL, on_delete=models.CASCADE)
    generation = models.ForeignKey('generation_BASCKETBALL', models.SET_NULL, null=True)
    position = models.ManyToManyField('position_BASCKETBALL', blank=True)
    date = models.DateTimeField('дата', default=timezone.now)
    matches_in_offers = models.IntegerField('кол-во матчей в контракте', default=1)

    class Meta:
        verbose_name = 'оффер'
        verbose_name_plural = 'офферы'

    def __str__(self):
        return f'оффер {self.pk}'

    # ################################# ################## ####################################
class position_BASCKETBALL(models.Model):
    position_name = models.CharField('позиция', max_length=55)
    image_position = models.ImageField('картинка позиции', blank=True, null=True, upload_to='position_BASCKETBALL/')

    class Meta:
        verbose_name = 'позиция'
        verbose_name_plural = 'позиции'
    def __str__(self):
        return f'{self.position_name}, {self.pk}'


class generation_BASCKETBALL(models.Model):
    generation_name = models.CharField('название состава', max_length=30, default='clown')

    class Meta:
        verbose_name = 'состав'
        verbose_name_plural = 'составы'

    def __str__(self):
        return f'{self.generation_name}, {self.pk}'

 # ################################# ############# #########################################

class cup_BASCKETBALL(models.Model):
    name = models.CharField('название', max_length=30,null=True,blank=True)
    image = models.ImageField('лого кубка', blank=True, null=True, upload_to='cup/basketball/')

    class Meta:
        verbose_name = 'кубок_комады'
        verbose_name_plural = 'кубки_команды'

    def __str__(self):
        return f'{self.name}'

class solo_cup_BASCKETBALL(models.Model):
    name = models.CharField('название', max_length=30,null=True,blank=True)
    image = models.ImageField('лого кубка', blank=True, null=True, upload_to='cup_solo/basketball/')

    class Meta:
        verbose_name = 'кубок_соло'
        verbose_name_plural = 'кубки_соло'

    def __str__(self):
        return f'{self.name}'