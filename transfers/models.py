from django.db import models
from users.models import User
from django.utils import timezone
from cash.models import direction

from b_unification.models.team import team


class transfer(models.Model):
    user = models.ForeignKey(User, models.CASCADE,null=True, blank=True)
    team = models.ForeignKey(team, models.SET_NULL, null=True)
    script = models.ForeignKey('script', models.SET_NULL, null=True)
    created_at = models.DateTimeField('дата создания', default=timezone.now)
    direction = models.ForeignKey(direction, models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'трансферы'
        verbose_name_plural = 'трансферы'
    def __str__(self):
        return f'{self.user}, {self.script}'

class script(models.Model):
    content = models.CharField('сценaрий', max_length=255)

    class Meta:
        verbose_name = 'сценарий'
        verbose_name_plural = 'сценарии'

    def __str__(self):
        return f'{self.content}'