from django.contrib import admin
from users import models



@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')

@admin.register(models.smail)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id',)

@admin.register(models.team_sap)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id',)

@admin.register(models.role)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(models.follow)
class UserAdmin(admin.ModelAdmin):
    list_display = ('by',)