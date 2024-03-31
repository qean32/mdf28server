from django.contrib import admin
from transfers import models


@admin.register(models.transfer_CS)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'team', 'script',)

@admin.register(models.transfer_DOTA)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'team', 'script',)

@admin.register(models.transfer_BASCKETBALL)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'team', 'script',)

@admin.register(models.script)
class UserAdmin(admin.ModelAdmin):
    list_display = ('content',)