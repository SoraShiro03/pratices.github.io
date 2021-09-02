from django.contrib import admin
from .models import AnimeList


@admin.register(AnimeList)
class AnimeListAdmin(admin.ModelAdmin):
   list_display = ('name', 'slug', 'image','date_posted')
   list_filter = ('date_posted',)
   search_fields = ('name', )
   prepopulated_fields = {'slug': ('name',)}
   date_hierarchy = 'date_posted'
   


