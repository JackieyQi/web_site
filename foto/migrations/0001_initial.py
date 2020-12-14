# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FotoPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150, verbose_name='title')),
                ('slug', models.SlugField(verbose_name='slug')),
                ('teaser', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='teaser', blank=True)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='body', blank=True)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='create_time', editable=False)),
                ('update_time', models.DateTimeField(verbose_name='update_time', null=True, editable=False, blank=True)),
                ('publish_time', models.DateTimeField(null=True, verbose_name='publish_time', blank=True)),
                ('state', models.IntegerField(default=2, verbose_name='state', choices=[(1, b'published'), (2, b'draft')])),
                ('secret_key', models.CharField(help_text='unique key for share url', unique=True, max_length=8, verbose_name='secret key', blank=True)),
                ('author', models.ForeignKey(related_name='foto_posts', verbose_name='author', to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)),
            ],
            options={
                'ordering': ('-publish_time',),
                'get_latest_by': 'publish_time',
                'verbose_name': 'FotoPost',
                'verbose_name_plural': 'FotoPosts',
            },
        ),
    ]
