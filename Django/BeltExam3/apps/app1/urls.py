from django.contrib import admin
from django.conf.urls import re_path, include
from . import views        
urlpatterns = [
    re_path(r'^$', views.index),
    re_path(r'^registration_process$', views.registration_process),
    re_path(r'^login_process$', views.login_process),
    re_path(r'^packages$', views.packages),
    re_path(r'^packages/new$', views.new),
    re_path(r'^packages/create$', views.create),
 #   re_path(r'^packages/(?P<package_id>\d+)/show$', views.show, name='show'),
    re_path(r'^packages/(?P<package_id>\d+)/edit$', views.edit, name='edit'),
    re_path(r'^packages/(?P<package_id>\d+)/update$', views.update, name='update'),
    re_path(r'^packages/(?P<package_id>\d+)/delete$', views.delete, name='delete')
]                
