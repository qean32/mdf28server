from django.db import models
from django.utils import timezone
from users.models import User
from direction.models import direction

# Create your models here.

class message(models.Model):
    author = models.ForeignKey(User, models.SET_NULL, null=True)
    content = models.CharField('сообщение', max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    image = models.ImageField('картинка', blank=True, null=True, upload_to='chat/')

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'
    def __str__(self):
        return f'{self.author}'