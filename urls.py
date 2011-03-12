from django.conf.urls.defaults import *  
from django.contrib.sitemaps import Sitemap
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()       

# google sitemaps :
sitemaps = {
	
}

# handler404 :
handler404 = 'IncidentRATP.frontend.views.handler_404'

urlpatterns = patterns('IncidentRATP.frontend.views',
    (r'^api/', include('IncidentRATP.api.urls')),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^services/?$', 'services'),
    (r'^incidents/(?P<scope>[a-z]*)', 'get_incidents'),
    (r'^incidents/?$', 'incidents'),
    (r'^incident/add', 'add_incident'),
    (r'^incident/detail/(?P<id>[0-9]*)/?$', 'get_incident'),
    (r'^incident/action/(?P<id>[0-9]*)/(?P<action>[a-z]*)', 'incident_interact'),
    (r'^contribuer/donation/?$', 'contribute_donate'),
    (r'^contribuer/twitter/?$', 'contribute_twitter'),
    (r'^contribuer/?$', 'contribute'),
    (r'^dev/iphone/?$', 'dev_iphone'),
	(r'^dev/android/?$', 'dev_android'),
    (r'^about/?$', 'about'),   
    (r'^home/?$', 'index'),
	(r'^stats/?$', 'stats'),
    (r'^dev/?$', 'dev'),
    (r'^/?$', 'index'),
)                                                       
urlpatterns += patterns('',
	(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
)

#local urls for serving media files during development
if settings.LOCAL_DEVELOPMENT:
    urlpatterns += patterns("django.views",
        url(r"%s(?P<path>.*)/$" % settings.MEDIA_URL[1:], "static.serve", {
            "document_root": settings.MEDIA_ROOT,
        })
    )