from django.db import models
from django.contrib.auth import get_user_model

from django.utils import timezone
User = get_user_model()


# Create your models here.

class post(models.Model):
    id = models.BigAutoField(primary_key=True)
    content = models.CharField('контент', max_length=255)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField('дата', default=timezone.now)
    image = models.ImageField('картинка', blank=True, null=True, upload_to='blog/image/')

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
    def __str__(self):
        return f'пост {self.id}'
