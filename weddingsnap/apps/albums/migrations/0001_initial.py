# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Album'
        db.create_table('albums_album', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal('albums', ['Album'])

        # Adding model 'Picture'
        db.create_table('albums_picture', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('album', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['albums.Album'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('path', self.gf('django.db.models.fields.files.ImageField')(default='img/no-picture.png', max_length=100)),
            ('thumbnail', self.gf('imagekit.models.fields.ProcessedImageField')(default='img/no-picture.png', max_length=100)),
        ))
        db.send_create_signal('albums', ['Picture'])


    def backwards(self, orm):
        # Deleting model 'Album'
        db.delete_table('albums_album')

        # Deleting model 'Picture'
        db.delete_table('albums_picture')


    models = {
        'albums.album': {
            'Meta': {'object_name': 'Album'},
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