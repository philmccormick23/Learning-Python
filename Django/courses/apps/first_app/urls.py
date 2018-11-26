from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^destroy/(?P<id>\d+)$', views.destroy, name='destroy'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete')


]  