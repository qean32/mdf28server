from django.contrib import admin
from transfers import models


@admin.register(models.transfer)
class UserAdmin(admin.ModelAdmin):
    list_display = ('script', 'id',)

@admin.register(models.script)
class UserAdmin(admin.ModelAdmin):
    list_display = ('content', 'id',)