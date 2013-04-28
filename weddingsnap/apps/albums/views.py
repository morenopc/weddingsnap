# -*- coding: UTF8 -*-
from albums import models
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template.loader import render_to_string
from django.template import RequestContext


# @login_required
def show_all_albums(request):
    """ Show all albums stored """

    albums = models.Album.objects.all()
    context = {'albums': albums}
    return render_to_response('albums/albums.html',
        context_instance=RequestContext(request, context))


# @login_required
def all_albums_json(request):
    """ Return all albums stored """

    return HttpResponse(
        render_to_string('albums/albums_json.html',
            {'albums': models.Album.objects.all()}),
        mimetype="application/json")


# @login_required
def album_pictures(request, album_id):
    """ Show album pictures """

    album = get_object_or_404(models.Album, id=album_id)
    pictures = models.Picture.objects.filter(album=album)
    context = {
        'album': album,
        'pictures': pictures
    }
    return render_to_response('albums/album_pictures.html',
        context_instance=RequestContext(request, context))


# @login_required
def album_pictures_json(request, album_id):
    """ Return album pictures in json format """

    album = get_object_or_404(models.Album, id=album_id)
    return HttpResponse(
        render_to_string('albums/album_pictures_json.html',
        {
            'album': album,
            'pictures': models.Picture.objects.filter(album=album)
        }),
        mimetype="application/json")
