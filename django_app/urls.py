from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       (r'^article/', include('articles.urls')),
                       url(r'^accounts/', include('userprofile.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^notifications/', include('notifications.urls')),
                       url(r'^login', 'django_app.views.login', name = 'login'),
                       url(r'^auth/$', 'django_app.views.auth_view', name = 'auth_view'),
                       url(r'^logout/$', 'django_app.views.logout', name = 'logout'),
                       url(r'^loggedin/$', 'django_app.views.loggedin', name = 'loggedin'),
                       url(r'^invalid/$', 'django_app.views.invalid', name = 'invalid'),
                       url(r'^registry/$', 'django_app.views.registry', name = 'registry'),
                       url(r'^registry_success/$', 'django_app.views.registry_success', name = 'registry_success'),
                       # Examples:
    # url(r'^$', 'django_app.views.home', name='home'),
    # url(r'^django_app/', include('django_app.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

)

# if settings.DEBUG:
#     urlpatterns += patterns('',
#                             r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}
#                             )