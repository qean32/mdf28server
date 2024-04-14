from django.contrib import admin
from direction.models import direction

# Register your models here.

@admin.register(direction)
class UserAdmin(admin.ModelAdmin):
    list_display = ('direction_name',)