from django.contrib import admin

# Register your models here.
from .models import Game, Move

# admin.site.register(Game)
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_dispplay =('id','first_player', 'second_player','status')
admin.site.register(Move)
