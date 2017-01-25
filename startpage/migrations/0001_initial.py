# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreateProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('user_name', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('current_rating', models.IntegerField()),
                ('rating_text', models.TextField()),
                ('bio', models.TextField()),
                ('zip_code', models.IntegerField()),
                ('website', models.URLField()),
            ],
        ),
    ]
