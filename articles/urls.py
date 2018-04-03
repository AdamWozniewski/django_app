from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^show_all/$', 'articles.views.articles'),
                       url(r'^(?P<article_id>\d+)/$', 'articles.views.article')
                       )