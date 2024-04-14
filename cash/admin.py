from django.contrib import admin
from cash import models

# Register your models here.

@admin.register(models.cash)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'price',)

@admin.register(models.list_cash)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id',)