from django.db import models

# Create your models here.

class direction(models.Model):
    direction_name = models.CharField('направление', max_length=55)

    class Meta:
        verbose_name = 'направление'
        verbose_name_plural = 'направления'
    def __str__(self):
        return f'{self.direction_name}'