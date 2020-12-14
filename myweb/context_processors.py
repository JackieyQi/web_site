# coding:utf8

from django.contrib.sites.shortcuts import get_current_site


def current_site(request):
    current_site = get_current_site(request)
    return {'SITE_DOMAIN': current_site.domain, 'SITE_NAME': current_site.name}
