# coding:utf8

from django.conf.urls import url
from foto.views import FotoIndexView, FotoDetailView, FotoDetailAdminView, DateBasePostDetailView


urlpatterns = [
    url(r"^$", FotoIndexView.as_view(), name="index"),
    url(r"^(?P<post_pk>\d+)/$", FotoDetailView.as_view(), name="foto_post_pk"),
    url(r"^(?P<post_secret_key>\w+)/$", FotoDetailAdminView.as_view(), name="foto_post_secret"),
]

urlpatterns += [
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
        DateBasePostDetailView.as_view(), name="foto_post"),
]
