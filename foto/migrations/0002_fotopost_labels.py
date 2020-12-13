# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0001_initial'),
        ('foto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotopost',
            name='labels',
            field=models.ManyToManyField(to='labels.YmeLabel'),
        ),
    ]
