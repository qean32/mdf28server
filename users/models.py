from django.contrib.auth.models import AbstractUser
from django.db import models
from users.api.managers import CustomUserManager
from colorfield.fields import ColorField
from django.utils import timezone


class User(AbstractUser):
    first_name = models.CharField('имя', max_length=55, blank=True, null=True)
    last_name = models.CharField('фамилия', max_length=55, blank=True, null=True)
    email = models.EmailField('почта', unique=True, max_length=255)
    username = models.CharField('никнейм', max_length=255, blank=True, null=True, unique=True)
    ava = models.ImageField('аватарка', blank=True, null=True, upload_to='users/ava/', default='/users/ava/default.png')
    background = models.ImageField('фон', blank=True, null=True, upload_to='users/background/', default='/users/background/default.png')
    status = models.CharField('статус', max_length=255, null=True, blank=True)
    smail = models.ForeignKey('smail', models.SET_NULL, null=True,blank=True)
    team_sap = models.ForeignKey('team_sap', models.SET_NULL, null=True,blank=True)

    telegram = models.CharField('tg', max_length=55, blank=True, null=True)
    steam = models.CharField('стим', max_length=255, blank=True, null=True)

    roles = models.ManyToManyField('role',blank=True)
    cups = models.ManyToManyField('cup',verbose_name='кубки команды', blank=True)

    is_org = models.BooleanField('организатор', default=False)
    is_BAN = models.BooleanField('БАН', default=False)
    created_at = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.pk})'

class follow(models.Model):
    for_r = models.ForeignKey(User,models.CASCADE, related_name='кто')
    by = models.ForeignKey(User,models.CASCADE, related_name='на')

class smail(models.Model):
    image = models.ImageField('смайлик', upload_to='users/smail/')

    class Meta:
        verbose_name = 'смайлик'
        verbose_name_plural = 'смайлики'

class team_sap(models.Model):
    image = models.ImageField('тим сап', upload_to='users/team_sap/')

    class Meta:
        verbose_name = 'сап тим'
        verbose_name_plural = 'сап тим'

class role(models.Model):
    name = models.CharField('роль', max_length=55)
    color = ColorField('цвет')

    class Meta:
        verbose_name = 'роль'
        verbose_name_plural = 'роли'

    def __str__(self):
        return f'{self.name}'
    
    
class cup(models.Model):
    name = models.CharField('название', max_length=30,null=True,blank=True)
    image = models.ImageField('лого кубка', blank=True, null=True, upload_to='cup/')

    class Meta:
        verbose_name = 'кубок'
        verbose_name_plural = 'кубки'

    def __str__(self):
        return f'{self.name}'