# -*- coding: UTF8 -*-
import requests
from albums import models
from facepy import utils, GraphAPI
from datetime import date, datetime, timedelta
from django.conf import settings
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.core.mail import send_mail
# Celery
# from celery.schedules import crontab
# from celery.task import periodic_task


def get_image_from_url(url):
    """ Get and save images from urls """
    r = requests.get(url)
    img_temp = NamedTemporaryFile(delete=True)
    img_temp.write(r.content)
    img_temp.flush()
    return File(img_temp)


# @periodic_task(run_every=crontab(minute='*/60'))
def hourly():
    """ Run every 60 minutes """
    albums = models.Album.objects.all().order_by('-create_at')[:1]
    if albums:
        count = albums[0].pictures().count()
        if count < 12:
            # Send email
            send_mail('Hourly albums email',
                    'Album {} has {} pictures'.format(albums[0].name, count),
                    settings.EMAIL_HOST_USER,
                    ['youremail@weddingsnap.com'], fail_silently=False)


# @periodic_task(run_every=crontab(minute='*/10'))
def fetch_pictures():
    """ Fetch pictures every 10 minutes """

    oauth_access_token = 'BAACEdEose0cBAFZCtR47HwYA7A9ZAOuekN4EZCQLDyQfyZA19uf0K4xIa8oBnrq8e8GdTcs80hpN5ZAoxzlHrRlvmXTJRdQCPtZAaD3IMrehFTL7kkTjADCDekwjLxfuK7M8EVMZBrrocwqfj8vrfHaRaiIaPoXBRoiTEJB2BeRxVZC7HZBc8luPE1k0phZB3jTR5K2An27MVx7YKT8ZA0gMD1DcuJ0XZAeROIyOVA4wUqSiqQZDZD'
    graph = GraphAPI(oauth_access_token)

    # get last album from facebook
    album = graph.get('me/albums?limit=1')
    albums = models.Album.objects.all().order_by('-create_at')[:1]
    # photos fql query
    full_album = 12
    limit = 5
    photos_fql = "SELECT src, created, modified FROM photo WHERE album_object_id = '{}' ORDER BY created DESC LIMIT {}"

    if albums and album['data']:
        album_id = album['data'][0].get('id')

        pictures_album = albums[0]
        pictures = pictures_album.pictures()
        count_pics = pictures.count()
        
        if count_pics == full_album:
            # Create new album
            pictures_album = models.Album(name=album['data'][0].get('name'))
            pictures_album.save()
            count_pics = 0
            # Send email
            send_mail('Album is full email',
                    'Album {} is full with {} pictures'.format(albums[0].name, count),
                    settings.EMAIL_HOST_USER,
                    ['youremail@weddingsnap.com'], fail_silently=False)
        else:
            if count_pics > 7:
                limit = full_album - count_pics

        # Get pictures
        photos = graph.fql(photos_fql.format(album_id, limit))
        for index, photo in enumerate(photos['data']):
            picture = models.Picture()
            picture.album = pictures_album
            picture.name = "picture_{}".format(count_pics + index + 1)
            picture.path.save(picture.name + '.jpg',
                get_image_from_url(photo.get('src')), save=True)
            picture.thumbnail = picture.path
            picture.save()

        pictures = pictures_album.pictures()
        # Set album cover
        if pictures_album.cover.name == 'img/no-cover-picture.png' and pictures:
           pictures_album.cover = pictures[0].thumbnail
           pictures_album.save()

    elif album['data']:
        # No albums
        album_id = album['data'][0].get('id')
        pictures_album = models.Album(name=album['data'][0].get('name'))
        pictures_album.save()

        photos = graph.fql(photos_fql.format(album_id, limit))
        for index, photo in enumerate(photos['data']):
            picture = models.Picture()
            picture.album = pictures_album
            picture.name = "picture_{}".format(count_pics + index)
            picture.path.save(picture.name + '.jpg',
                get_image_from_url(photo.get('src')), save=True)
            picture.thumbnail.save(picture.name + '.jpg',
                get_image_from_url(photo.get('src')), save=True)
            picture.save()

        pictures = pictures_album.pictures()
        # Set album cover
        if pictures:
           pictures_album.cover = pictures[0].thumbnail
           pictures_album.save()
