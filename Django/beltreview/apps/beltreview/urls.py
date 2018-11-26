from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^books$', views.success),
    url(r'^login$', views.login),
    url(r'^books/add$', views.add),
    url(r'^books/addBook$', views.addBook),
    url(r'^books/(?P<id>\d+)$', views.number, name='newbook'),
    url(r'^books/addReview$', views.addReview)
]