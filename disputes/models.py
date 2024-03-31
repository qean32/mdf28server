from django.db import models
from django.utils import timezone
from users.models import User
from cash.models import direction

# Create your models here.
class disput(models.Model):
    author = models.ForeignKey(User, models.SET_NULL, null=True,  related_name='authorL')
    created_at = models.DateTimeField(default=timezone.now)
    title = models.CharField('тема', max_length=255)
    content = models.CharField('сообщение', max_length=255,blank=True,null=True)
    is_of = models.BooleanField('закрыт вопрос', default=False)
    class Meta:
        verbose_name = 'диспут'
        verbose_name_plural = 'диспуты'

class message(models.Model):
    author = models.ForeignKey(User, models.SET_NULL, null=True,  related_name='oauthor')
    content = models.CharField('сообщение', max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    image = models.ImageField('картинка', blank=True, null=True, upload_to='disputes/image/')
    is_message_org =  models.BooleanField('сообщение от организатора', default=False)
    disput = models.ForeignKey(disput,models.SET_NULL, null=True,  related_name='aeruthorL')

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'

    def __str__(self):
        return f'диспут № {self.id}, {self.author}'