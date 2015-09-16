# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('visit_stamp', models.DateTimeField(auto_now_add=True)),
                ('user_agent', models.CharField(max_length=255)),
            ],
        ),
    ]
