from django.contrib import admin
from news.models import post,like,coment

# Register your models here.


@admin.register(post)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'author',)

@admin.register(like)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'author',)

@admin.register(coment)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'author',)
