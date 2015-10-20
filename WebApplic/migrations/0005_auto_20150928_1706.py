# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebApplic', '0004_titles'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Titles',
            new_name='Title',
        ),
        migrations.AlterModelTable(
            name='title',
            table='Title',
        ),
    ]
