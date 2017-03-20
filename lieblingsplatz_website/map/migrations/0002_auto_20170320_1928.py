# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kita',
            name='extra_address_line',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='kita',
            name='friday_close',
            field=models.CharField(blank=True, max_length=31),
        ),
        migrations.AddField(
            model_name='kita',
            name='friday_open',
            field=models.CharField(blank=True, max_length=31),
        ),
        migrations.AddField(
            model_name='kita',
            name='monday_close',
            field=models.CharField(blank=True, max_length=31),
        ),
        migrations.AddField(
            model_name='kita',
            name='monday_open',
            field=models.CharField(blank=True, max_length=31),
        ),
        migrations.AddField(
            model_name='kita',
            name='saturday_close',
            field=models.CharField(blank=True, max_length=31),
        ),
        migrations.AddField(
            model_name='kita',
            name='saturday_open',
            field=models.CharField(blank=True, max_length=31),
        ),
        migrations.AddField(
            model_name='kita',
            name='sunday_close',
            field=models.CharField(blank=True, max_length=31),
        ),
        migrations.AddField(
            model_name='kita',
            name='sunday_open',
            field=models.CharField(blank=True, max_length=31),
        ),
        migrations.AddField(
            model_name='kita',
            name='thursday_close',
            field=models.CharField(blank=True, max_length=31),
        ),
        migrations.AddField(
            model_name='kita',
            name='thursday_open',
            field=models.CharField(blank=True, max_length=31),
        ),
        migrations.AddField(
            model_name='kita',
            name='tuesday_close',
            field=models.CharField(blank=True, max_length=31),
        ),
        migrations.AddField(
            model_name='kita',
            name='tuesday_open',
            field=models.CharField(blank=True, max_length=31),
        ),
        migrations.AddField(
            model_name='kita',
            name='wednesday_close',
            field=models.CharField(blank=True, max_length=31),
        ),
        migrations.AddField(
            model_name='kita',
            name='wednesday_open',
            field=models.CharField(blank=True, max_length=31),
        ),
        migrations.AlterField(
            model_name='kita',
            name='agency',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='kita',
            name='city',
            field=models.CharField(max_length=255, default='Berlin'),
        ),
        migrations.AlterField(
            model_name='kita',
            name='email',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='kita',
            name='extras',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='kita',
            name='focus',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='kita',
            name='kind_of_agency',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='kita',
            name='kind_of_facility',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='kita',
            name='multilingualism',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='kita',
            name='pedagogics',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='kita',
            name='phonenumber',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='kita',
            name='senats_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='kita',
            name='website',
            field=models.URLField(blank=True),
        ),
    ]
