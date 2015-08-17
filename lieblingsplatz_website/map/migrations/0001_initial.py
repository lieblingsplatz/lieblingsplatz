# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kita',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.TextField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('address', models.TextField()),
                ('zip_code', models.IntegerField()),
                ('district', models.TextField()),
                ('senats_id', models.IntegerField()),
            ],
        ),
    ]
