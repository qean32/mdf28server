from django.contrib import admin
from generation.models import generation

# Register your models here.

@admin.register(generation)
class UserAdmin(admin.ModelAdmin):
    list_display = ('generation_name',)