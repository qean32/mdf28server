from django.db import models
from users.models import User
from django.utils import timezone
from cash.models import direction

from bascketball.models.team import team_BASCKETBALL
from cs.models.team import team_CS
from dota.models.team import team_DOTA


class transfer_DOTA(models.Model):
    user = models.ForeignKey(User, models.CASCADE,null=True, blank=True)
    team = models.ForeignKey(team_DOTA, models.SET_NULL, null=True)
    script = models.ForeignKey('script', models.SET_NULL, null=True)
    date_crate = models.DateTimeField('дата создания', default=timezone.now)

    class Meta:
        verbose_name = 'трансферы_DOTA'
        verbose_name_plural = 'трансферы_DOTA'
    def __str__(self):
        return f'{self.user}, {self.script}'

class transfer_CS(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    team = models.ForeignKey(team_CS, models.SET_NULL, null=True)
    script = models.ForeignKey('script', models.SET_NULL, null=True)
    date_crate = models.DateTimeField('дата создания', default=timezone.now)

    class Meta:
        verbose_name = 'трансферы_CS'
        verbose_name_plural = 'трансферы_CS'
    def __str__(self):
        return f'{self.user}, {self.script}'

class transfer_BASCKETBALL(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    team = models.ForeignKey(team_BASCKETBALL, models.SET_NULL, null=True)
    script = models.ForeignKey('script', models.SET_NULL, null=True)
    date_crate = models.DateTimeField('дата создания', default=timezone.now)

    class Meta:
        verbose_name = 'трансферы_BASCKETBALL'
        verbose_name_plural = 'трансферы_BASCKETBALL'
    def __str__(self):
        return f'{self.user}, {self.script}'

class script(models.Model):
    content = models.CharField('сценaрий', max_length=255)

    class Meta:
        verbose_name = 'сценарий'
        verbose_name_plural = 'сценарии'

    def __str__(self):
        return f'{self.content}'