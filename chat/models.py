from django.db import models
from django.utils import timezone
from users.models import User
from direction.models import direction

# Create your models here.

class message(models.Model):
    author = models.ForeignKey(User, models.SET_NULL, null=True)
    content = models.CharField('сообщение', max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    direction = models.ForeignKey(direction,  on_delete=models.SET_NULL, null=True, blank=True,related_name='direction_1')
    image = models.ImageField('картинка', blank=True, null=True, upload_to='chat/image/')
    is_message_org =  models.BooleanField('сообщение от организатора', default=False)
    is_answer =  models.BooleanField('сообщение ответ', default=False)
    is_answer_for = models.ForeignKey('message', models.SET_NULL, null=True,blank=True)

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'
    def __str__(self):
        return f'{self.author}, {self.is_message_org}'

class like_m(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,related_name='author_like_m')
    message = models.ForeignKey(message, on_delete=models.SET_NULL, null=True, blank=True,related_name='post_one_m')

    class Meta:
        verbose_name = 'лайк'
        verbose_name_plural = 'лайки'
        unique_together = (('author', 'message'),)

    def __str__(self):
        return f'{self.author} ({self.message})'