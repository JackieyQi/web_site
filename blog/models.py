# coding:utf8

from random import choice

import pytz
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

try:
    from string import letters
except ImportError:
    from string import ascii_letters as letters

from labels.models import YmeLabel

STATE_CHOICE = [(1, "published"), (2, "draft")]


class BlogPostManager(models.Manager):
    def published(self):
        return self.filter(publish_time__lte=timezone.now(), state=1)

    def current(self):
        return self.published().order_by("-publish_time")


class BlogPost(models.Model):
    title = models.CharField(_("title"), max_length=150)
    slug = models.SlugField(_("slug"))
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="blog_posts",
        verbose_name=_("author"),
        on_delete=models.CASCADE,
    )

    labels = models.ManyToManyField(
        YmeLabel, blank=True, related_name="blog_posts", verbose_name=_("YmeLabel")
    )

    teaser = RichTextUploadingField(_("teaser"), editable=True, blank=True)
    body = RichTextUploadingField(_("body"), blank=True)

    create_time = models.DateTimeField(
        _("create_time"), default=timezone.now, editable=False
    )
    update_time = models.DateTimeField(
        _("update_time"), null=True, blank=True, editable=False
    )
    publish_time = models.DateTimeField(_("publish_time"), null=True, blank=True)
    state = models.IntegerField(
        _("state"), choices=STATE_CHOICE, default=STATE_CHOICE[-1][0]
    )

    secret_key = models.CharField(
        _("secret key"),
        max_length=8,
        blank=True,
        unique=True,
        help_text=_("unique key for share url"),
    )

    objects = BlogPostManager()

    class Meta:
        ordering = ("-publish_time",)
        get_latest_by = "publish_time"
        verbose_name = _("BlogPost")
        verbose_name_plural = _("BlogPosts")

    def __str__(self):
        return self.title

    @property
    def is_published(self):
        return self.state == STATE_CHOICE[0][0]

    @property
    def share_url(self):
        if not self.is_published:
            if self.secret_key:
                return reverse(
                    "yme_blog:blog_post_secret",
                    kwargs={"post_secret_key": self.secret_key},
                )
            else:
                return "保存文档自动生成链接"
        else:
            return self.get_absolute_url()

    def get_absolute_url(self):
        if not self.is_published:
            name = "yme_blog:blog_post_pk"
            kwargs = {"post_pk": self.pk}
        else:
            name = "yme_blog:blog_post"
            if settings.USE_TZ and settings.TIME_ZONE:
                publish_time = pytz.timezone(settings.TIME_ZONE).normalize(
                    self.publish_time
                )
            else:
                publish_time = self.publish_time
            kwargs = {
                "year": publish_time.strftime("%Y"),
                "month": publish_time.strftime("%m"),
                "day": publish_time.strftime("%d"),
                "slug": self.slug,
            }
        return reverse(name, kwargs=kwargs)

    def get_app_url(self):
        return reverse("yme_blog:index")

    def get_app_name(self):
        return _("blog")

    def save(self, **kwargs):
        if not self.secret_key:
            # 随即密钥生成
            self.secret_key = "".join(choice(letters) for _ in range(8))

        if self.is_published and self.publish_time is None:
            self.publish_time = timezone.now()
        super(BlogPost, self).save(**kwargs)
