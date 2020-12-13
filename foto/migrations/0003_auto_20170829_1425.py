# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foto', '0002_fotopost_labels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotopost',
            name='labels',
            field=models.ManyToManyField(related_name='foto_posts', null=True, verbose_name='YmeLabel', to='labels.YmeLabel', blank=True),
        ),
    ]
