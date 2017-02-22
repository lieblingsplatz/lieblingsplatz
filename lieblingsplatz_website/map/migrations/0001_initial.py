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
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.TextField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('address', models.TextField()),
                ('zip_code', models.IntegerField()),
                ('city', models.TextField()),
                ('district', models.TextField()),
                ('senats_id', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField()),
                ('kind_of_facility', models.TextField()),
                ('agency', models.TextField()),
                ('kind_of_agency', models.TextField()),
                ('pedagogics', models.TextField()),
                ('focus', models.TextField()),
                ('multilingualism', models.TextField()),
                ('extras', models.TextField()),
            ],
        ),
    ]
