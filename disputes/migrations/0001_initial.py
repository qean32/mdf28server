# Generated by Django 4.2.7 on 2024-05-16 06:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='disput',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('title', models.CharField(max_length=255, verbose_name='тема')),
                ('content', models.CharField(blank=True, max_length=255, null=True, verbose_name='сообщение')),
                ('is_of', models.BooleanField(default=False, verbose_name='закрыт вопрос')),
            ],
            options={
                'verbose_name': 'диспут',
                'verbose_name_plural': 'диспуты',
            },
        ),
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255, verbose_name='сообщение')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(blank=True, null=True, upload_to='disputes/image/', verbose_name='картинка')),
                ('is_message_org', models.BooleanField(default=False, verbose_name='сообщение от организатора')),
            ],
            options={
                'verbose_name': 'сообщение',
                'verbose_name_plural': 'сообщения',
            },
        ),
    ]
