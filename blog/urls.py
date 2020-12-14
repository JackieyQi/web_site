# coding:utf8

from django.conf.urls import url
from blog.views import (BlogIndexView, BlogDetailView,
                        BlogDetailAdminView, DateBasePostDetailView)


urlpatterns = [
    url(r'^$', BlogIndexView.as_view(), name="index"),
    url(r'^(?P<post_pk>\d+)/$', BlogDetailView.as_view(), name="blog_post_pk"),
    url(
        r'^(?P<post_secret_key>\w+)/$',
        BlogDetailAdminView.as_view(), name="blog_post_secret"
    ),
]

urlpatterns += [
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
        DateBasePostDetailView.as_view(), name="blog_post"),
]
