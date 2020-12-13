# coding:utf8

from django.contrib import admin

from .models import YmeLabel


@admin.register(YmeLabel)
class YmeLabelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",), }
