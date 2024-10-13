from django.contrib import admin
from chat import models

# Register your models here.


@admin.register(models.message)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'author',)
