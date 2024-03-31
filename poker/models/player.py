from django.db import models
from users.models import User
from django.utils import timezone

class player_POKER(models.Model):
    user = models.OneToOneField(User, models.CASCADE, primary_key=True)
    date_joined = models.DateField('дата присоединения', default=timezone.now)

    # ################################# ################# #####################################

    matches = models.IntegerField('кол-во матчей', default=0)
    win_matches = models.IntegerField('кол-во побед матчи', default=0)
    tournament = models.IntegerField('кол-во турниров', default=0)
    win_tournament = models.IntegerField('кол-во побед турнир', default=0)
    is_recognized = models.BooleanField('признанный игрок', default=False)


    class Meta:
        verbose_name = 'Игрок_POKER'
        verbose_name_plural = 'Игроки_POKER'

    def __str__(self):
        return f'Игрок_POKER #_{self.user}, {self.pk}'