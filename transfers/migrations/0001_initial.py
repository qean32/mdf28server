# Generated by Django 4.2.7 on 2024-05-16 06:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('direction', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='script',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255, verbose_name='сценaрий')),
            ],
            options={
                'verbose_name': 'сценарий',
                'verbose_name_plural': 'сценарии',
            },
        ),
        migrations.CreateModel(
            name='transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='дата создания')),
                ('direction', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='direction.direction')),
                ('script', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='transfers.script')),
            ],
            options={
                'verbose_name': 'трансферы',
                'verbose_name_plural': 'трансферы',
            },
        ),
    ]