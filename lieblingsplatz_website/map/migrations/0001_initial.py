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
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('address', models.CharField(max_length=255)),
                ('zip_code', models.IntegerField()),
                ('city', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=255)),
                ('senats_id', models.IntegerField()),
                ('phonenumber', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('website', models.URLField()),
                ('kind_of_facility', models.CharField(max_length=255)),
                ('agency', models.CharField(max_length=255)),
                ('kind_of_agency', models.CharField(max_length=255)),
                ('pedagogics', models.TextField()),
                ('focus', models.TextField()),
                ('multilingualism', models.TextField()),
                ('extras', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('phonenumber', models.CharField(max_length=31)),
                ('kita', models.ForeignKey(to='map.Kita')),
            ],
        ),
    ]
