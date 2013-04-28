# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Picture.stored_at'
        db.add_column('albums_picture', 'stored_at',
                      self.gf('django.db.models.fields.DateField')(auto_now_add=True, default=datetime.datetime(2013, 4, 28, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Picture.stored_at'
        db.delete_column('albums_picture', 'stored_at')


    models = {
        'albums.album': {
            'Meta': {'object_name': 'Album'},
            'cover': ('imagekit.models.fields.ProcessedImageField', [], {'default': "'img/no-cover-picture.png'", 'max_length': '100'}),
            'create_at': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'albums.picture': {
            'Meta': {'object_name': 'Picture'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['albums.Album']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'path': ('django.db.models.fields.files.ImageField', [], {'default': "'img/no-picture.png'", 'max_length': '100'}),
            'stored_at': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'thumbnail': ('imagekit.models.fields.ProcessedImageField', [], {'default': "'img/no-picture.png'", 'max_length': '100'})
        }
    }

    complete_apps = ['albums']