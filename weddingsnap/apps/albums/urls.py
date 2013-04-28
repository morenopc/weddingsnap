# -*- coding: UTF8 -*-
from django.conf.urls.defaults import *


urlpatterns = patterns('albums.views',
    url(r'^$', 'show_all_albums', name='show_all_albums'),
    # Albums JSON
    url(r'^all/json', 'all_albums_json', name='all_albums_json'),
    # Albums
    url(r'^all', 'show_all_albums', name='show_all_albums'),
    # Pictures JSON
    url(r'^(?P<album_id>\d+)/pictures/json', 'album_pictures_json',
        name='album_pictures_json'),
    # Pictures
    url(r'^(?P<album_id>\d+)/pictures', 'album_pictures',
        name='album_pictures'),
)
