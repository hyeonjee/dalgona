from django.contrib import admin
from.models import Game

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'view_count',
        'created_at',
        'updated_at',
    )
