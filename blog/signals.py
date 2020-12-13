# coding:utf8

from django.dispatch import Signal


post_published = Signal(providing_args=["post"])
