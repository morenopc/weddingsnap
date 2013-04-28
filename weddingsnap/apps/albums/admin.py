# -*- coding: UTF8 -*-
from django.contrib import admin
from albums import models


class AlbumAdmin(admin.ModelAdmin):
    pass
admin.site.register(models.Album, AlbumAdmin)


class PictureAdmin(admin.ModelAdmin):
    pass
admin.site.register(models.Picture, PictureAdmin)
