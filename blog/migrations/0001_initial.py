# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'blog/static/gochiusa')),
                ('name', models.CharField(max_length=b'20')),
                ('birth', models.CharField(max_length=b'20')),
                ('stature', models.CharField(max_length=b'20')),
                ('blood_type', models.CharField(max_length=b'20')),
            ],
        ),
    ]
