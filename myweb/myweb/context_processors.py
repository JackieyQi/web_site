# from django.contrib.sites.models import get_current_site
from django.contrib.sites.shortcuts import get_current_site


def current_site(request):
	return {'current_site': get_current_site(request)}