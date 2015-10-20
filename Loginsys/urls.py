__author__ = 'yura'

from django.conf.urls import include, url

urlpatterns = [
    url(r'^login/', 'Loginsys.views.login'),
    url(r'^logout/', 'Loginsys.views.logout'),
    url(r'^register/', 'Loginsys.views.register'),
]