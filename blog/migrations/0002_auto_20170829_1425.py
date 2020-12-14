# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='labels',
            field=models.ManyToManyField(related_name='blog_posts', null=True, verbose_name='YmeLabel', to='labels.YmeLabel', blank=True),
        ),
    ]
