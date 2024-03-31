from django.db import models
from django.utils import timezone
from users.models import User

# Create your models here.

class list_cash(models.Model):
    price = models.IntegerField('бюджет', null=True)

    class Meta:
        verbose_name = 'бюджет'
        verbose_name_plural = 'бюджет'
    def __str__(self):
        return f'бюджет {self.price}'

class cash(models.Model):
    author = models.ForeignKey(User, models.SET_NULL, null=True)
    price = models.IntegerField('цена',)
    content = models.CharField('на что', max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    direction = models.ForeignKey('direction', models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'трата'
        verbose_name_plural = 'траты'
    def __str__(self):
        return f'{self.price}, {self.content}'

class direction(models.Model):
    direction_name = models.CharField('направление', max_length=55)

    class Meta:
        verbose_name = 'направление'
        verbose_name_plural = 'направления'
    def __str__(self):
        return f'{self.direction_name}'