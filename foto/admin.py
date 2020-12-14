# coding:utf8

from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now

from .models import FotoPost
from .forms import FotoPostAdminForm


@admin.register(FotoPost)
class FotoPostAdmin(admin.ModelAdmin):
    list_display = ("title", "state", "publish_time", "get_share_url")
    list_filter = ("state",)
    actions = ("make_published",)
    fields = ("title", "slug", "author", "labels", "teaser", "body", "share_url", "state", "publish_time")
    readonly_fields = ("share_url",)
    form = FotoPostAdminForm

    prepopulated_fields = {"slug": ("title",)}

    def get_share_url(self, obj):
        return format_html("<a href='%s'>%s</a>" % (obj.share_url, obj.share_url))

    get_share_url.short_description = _("share url")
    get_share_url.allow_tags = True

    def make_published(self, request, queryset):
        rows = queryset.update(state=1, publish_time=now())
        self.message_user(request, "%s posts successfully marked as published." % rows)

    make_published.short_description = "Mark selected as published"
