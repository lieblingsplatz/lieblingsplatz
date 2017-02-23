# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('phonenumber', models.CharField(max_length=31)),
            ],
        ),
        migrations.AlterField(
            model_name='kita',
            name='address',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='kita',
            name='agency',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='kita',
            name='city',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='kita',
            name='district',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='kita',
            name='email',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='kita',
            name='kind_of_agency',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='kita',
            name='kind_of_facility',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='kita',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AddField(
            model_name='phone',
            name='kita',
            field=models.ForeignKey(to='map.Kita'),
        ),
    ]
