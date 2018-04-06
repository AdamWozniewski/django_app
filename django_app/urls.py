from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^article/', include('articles.urls')),
    # Examples:
    # url(r'^$', 'django_app.views.home', name='home'),
    # url(r'^django_app/', include('django_app.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
   url(r'^admin/', include(admin.site.urls)),
                       url(r'^accounts/login/$', include('django_app.views.login')),
                       url(r'^accounts/auth/$', include('django_app.views.auth.login')),
                       url(r'^accounts/logout/$', include('django_app.views.logout')),
                       url(r'^accounts/leggedin/$', include('django_app.views.loggedin')),
                       url(r'^accounts/auth/$', include('django_app.views.invalid_login')),
)

# if settings.DEBUG:
#     urlpatterns += patterns('',
#                             r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}
#                             )