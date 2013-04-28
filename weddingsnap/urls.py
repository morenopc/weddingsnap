from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    # Albums
    url(r'^$', include('albums.urls')),
    url(r'^album/', include('albums.urls')),
    url(r'^albums/', include('albums.urls')),
)
# Media
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': settings.MEDIA_ROOT }),
    )
