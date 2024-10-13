from django.contrib import admin
from disputes import models

# Register your models here.


@admin.register(models.message)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'author',)

@admin.register(models.disput)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'author',)