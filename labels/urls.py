# coding:utf8

from django.conf.urls import url

from .views import LabelIndexView


urlpatterns = [
    url(r'^(?P<label>[-\w]+)/$', LabelIndexView.as_view(), name="label"),

]
