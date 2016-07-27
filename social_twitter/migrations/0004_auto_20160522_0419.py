# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-22 04:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_twitter', '0003_added_sentimet_and_score_to_tweet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='sentiment',
            field=models.CharField(blank=True, choices=[('positive', 'positive'), ('negative', 'negative'), ('neutral', 'neutral')], max_length=15),
        ),
    ]
