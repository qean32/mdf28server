from django.db import models
from users.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

from colorfield.fields import ColorField
from direction.models import direction

# ################################# ##################### #################################

class team(models.Model):

    name = models.CharField('название команды', max_length=30, default='clown`s', unique=True)

    logo = models.ImageField('лого команды', blank=True, null=True, upload_to='team/logo/', default='/team/logo/default.png')
    background = models.ImageField('фон', blank=True, null=True, upload_to='team/background/', default='/team/background/default.png')

    status = models.CharField('статус', max_length=255, null=True, blank=True)
    detail = models.CharField('подробно', max_length=255, null=True, blank=True)
    cups = models.ManyToManyField('cup',verbose_name='кубки команды', blank=True)

    director = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    created_at = models.DateTimeField('дата создания', default=timezone.now)
    
    is_recognized = models.BooleanField('признанная команда', default=False)
    direction = models.ForeignKey(direction,  on_delete=models.SET_NULL, null=True, blank=True,related_name='dir124ection21_12')

    class Meta:
        verbose_name = 'команда'
        verbose_name_plural = 'команды'

    def __str__(self):
        return f'{self.name}, {self.pk}'

# ################################# ################### ###################################

class offers(models.Model):
    is_view = models.BooleanField('просмотр', default=False)
    user = models.ForeignKey(User, models.CASCADE)

    team = models.ForeignKey(team, on_delete=models.CASCADE)

    created_at = models.DateTimeField('дата создания', default=timezone.now)
    matches_in_offers = models.IntegerField('кол-во матчей в контракте', default=10)
    direction = models.ForeignKey(direction,  on_delete=models.SET_NULL, null=True, blank=True,related_name='dir124ecti1on_12')


    class Meta:
        verbose_name = 'оффер'
        verbose_name_plural = 'офферы'

    def __str__(self):
        return f'оффер {self.team}'

    # ################################# ################## ####################################


class rank(models.Model):
    name = models.CharField('ранг', max_length=55)
    image = models.ImageField('картинка ранга', blank=True, null=True, upload_to='rank/')

    class Meta:
        verbose_name = 'ранг'
        verbose_name_plural = 'ранги'

    def __str__(self):
        return f'{self.name}, {self.pk}'

 # ################################# ############# #########################################

class cup(models.Model):
    name = models.CharField('название', max_length=30,null=True,blank=True)
    image = models.ImageField('лого кубка', blank=True, null=True, upload_to='cup/')

    class Meta:
        verbose_name = 'кубок'
        verbose_name_plural = 'кубки'

    def __str__(self):
        return f'{self.name}'