__author__ = 'yura'

from django.conf.urls import include, url

urlpatterns = [
    url(r'^1/', 'WebApplic.views.basic_one'),
    url(r'^2/', 'WebApplic.views.template_two'),
    url(r'^3/', 'WebApplic.views.template_three_simple'),
    url(r'^posts/get/(?P<post_id>\d+)/$', 'WebApplic.views.post'),
    url(r'^title/', 'WebApplic.views.title_settings'),
    url(r'^addlike/(\d+)/(\d+)/$', 'WebApplic.views.addlike'),
    url(r'^addcomment/(?P<post_id>\d+)/$', 'WebApplic.views.addcomment'),
    url(r'^allposts/(\d+)/$', 'WebApplic.views.posts'),
    url(r'^', 'WebApplic.views.posts'),
]