from django.contrib import admin
from .models import *


class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'time_created', 'photo', 'published')
    list_display_links = ('id', 'name')
    list_editable = ('published',)
    list_filter = ('time_created',)
    search_fields = ('name', 'description')


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Genre, GenreAdmin)
