# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebApplic', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='post',
            table='Posts',
        ),
    ]
