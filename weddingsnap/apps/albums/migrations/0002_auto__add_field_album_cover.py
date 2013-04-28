# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Album.cover'
        db.add_column('albums_album', 'cover',
                      self.gf('imagekit.models.fields.ProcessedImageField')(default='img/no-cover-picture.png', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Album.cover'
        db.delete_column('albums_album', 'cover')


    models = {
        'albums.album': {
            'Meta': {'object_name': 'Album'},
            'cover': ('imagekit.models.fields.ProcessedImageField', [], {'default': "'img/no-cover-picture.png'", 'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'albums.picture': {
            'Meta': {'object_name': 'Picture'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['albums.Album']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'path': ('django.db.models.fields.files.ImageField', [], {'default': "'img/no-picture.png'", 'max_length': '100'}),
            'thumbnail': ('imagekit.models.fields.ProcessedImageField', [], {'default': "'img/no-picture.png'", 'max_length': '100'})
        }
    }

    complete_apps = ['albums']