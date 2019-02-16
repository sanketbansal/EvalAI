# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-15 23:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0043_add_max_docker_image_size_for_challenge'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='evaluate_concurrent_max_submissions',
            field=models.PositiveIntegerField(default=100000),
        ),
    ]
