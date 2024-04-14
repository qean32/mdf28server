from django.db import models

# Create your models here.

class generation(models.Model):
    generation_name = models.CharField('название состава', max_length=30, default='clown')

    class Meta:
        verbose_name = 'состав'
        verbose_name_plural = 'составы'

    def __str__(self):
        return f'{self.generation_name}, {self.pk}'