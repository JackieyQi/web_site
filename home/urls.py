# coding:utf8

from django.conf.urls import url

from .views import HomeIndexView


urlpatterns = [
    url(r'^$', HomeIndexView.as_view(), name="index"),

]
