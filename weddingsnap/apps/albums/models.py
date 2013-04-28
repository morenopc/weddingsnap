# -*- coding: UTF8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit, Adjust


class Album(models.Model):
    """ Albums model """
    DEFAULT_COVER = 'img/no-cover-picture.png'
    create_at = models.DateField(_('create at'), auto_now_add=True)
    name = models.CharField(max_length=64)
    cover = ProcessedImageField(
        [Adjust(contrast=1.2, sharpness=1.1), ResizeToFit(200, 200)],
        options={'quality': 90},
        upload_to='albums/covers',
        default=DEFAULT_COVER)

    def pictures(self, ):
        return Picture.objects.filter(album=self)

    def __unicode__(self):
        return self.name


class Picture(models.Model):
    """ Album pictures """
    DEFAULT_PICTURE = 'img/no-picture.png'
    album = models.ForeignKey(Album, verbose_name=_('album'))
    name = models.CharField(_('name'), max_length=64)
    path = models.ImageField(upload_to='albums/pictures',
        default=DEFAULT_PICTURE)
    thumbnail = ProcessedImageField(
        [Adjust(contrast=1.2, sharpness=1.1), ResizeToFit(200, 200)],
        options={'quality': 90},
        upload_to='albums/pictures/thumbnails',
        default=DEFAULT_PICTURE)
    stored_at = models.DateField(_('stored at'), auto_now_add=True)

    def __unicode__(self):
        return self.name
