# Generated by Django 4.2.7 on 2024-04-14 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dota', '0005_hero_hero_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='record_stat',
            name='first_team',
            field=models.BooleanField(default=False, verbose_name='1 тим'),
        ),
    ]