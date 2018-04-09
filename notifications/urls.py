from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^show/(?P<notification_id>\d+)/$', 'notifications.views.show_notification'),
                       url(r'^delete/(?P<notification_id>\d+)/$', 'notifications.views.delete_notification')
                       )