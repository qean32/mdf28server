from django.db import models
from django.contrib.auth import get_user_model

from django.utils import timezone
User = get_user_model()
from direction.models import direction


# Create your models here.

class post(models.Model):
    content = models.CharField('контент', max_length=255)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='author_post')
    created_at = models.DateTimeField(default=timezone.now)
    image = models.ImageField('картинка', blank=True, null=True, upload_to='news/image/')
    direction = models.ForeignKey(direction,  on_delete=models.SET_NULL, null=True, blank=True,related_name='direction_2')

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'

    def __str__(self):
        return f'{self.author} ({self.direction})'

class like(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,related_name='author_like')
    postt = models.ForeignKey(post, on_delete=models.SET_NULL, null=True, blank=True,related_name='post_like')

    class Meta:
        verbose_name = 'лайк'
        verbose_name_plural = 'лайки'
        unique_together = (('author','postt',),)

    def __str__(self):
        return f'{self.author} ({self.postt})'

class coment(models.Model):
    content = models.CharField('контент', max_length=255)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,related_name='author_coment')
    post = models.ForeignKey(post, on_delete=models.SET_NULL, null=True, blank=True,related_name='post_coment')
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'комент'
        verbose_name_plural = 'коменты'

    def __str__(self):
        return f'{self.author}'