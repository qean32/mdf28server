# Generated by Django 4.2.7 on 2024-05-16 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('b_unification', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='team/position/', verbose_name='лого команды'),
        ),
    ]
