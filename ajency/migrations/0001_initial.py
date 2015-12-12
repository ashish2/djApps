# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(default=None)),
                ('name', models.CharField(default=None, max_length=512, null=True)),
                ('slug', models.SlugField(default=None, max_length=128, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(default=None)),
                ('name', models.CharField(default=None, max_length=512, null=True)),
                ('slug', models.SlugField(default=None, max_length=128, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(default=None)),
                ('title', models.CharField(default=None, max_length=512, null=True)),
                ('description', models.TextField(default=None, blank=True)),
                ('image', models.ImageField(upload_to=b'uploads/')),
                ('length', models.IntegerField(default=None, null=True, blank=True)),
                ('release_date', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(default=None, max_length=128, blank=True)),
                ('categories', models.ManyToManyField(to='ajency.Categories')),
                ('languages', models.ManyToManyField(to='ajency.Languages')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
