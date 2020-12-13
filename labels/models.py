# coding:utf8

from django.db import models
from django.utils.translation import ugettext_lazy as _


class YmeLabelManager(models.Manager):
    def current(self):
        return self.filter(enabled=True)


class YmeLabel(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(unique=True)
    enabled = models.BooleanField(default=True)

    objects = YmeLabelManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("YmeLabel")
        verbose_name_plural = _("YmeLabels")
