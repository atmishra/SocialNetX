# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-21 20:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_twitter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='percentage',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
        ),
        migrations.AddField(
            model_name='tweet',
            name='sentiment',
            field=models.CharField(blank=True, choices=[('POS', 'Positive'), ('NEG', 'Negative'), ('NET', 'Neutral')], max_length=3),
        ),
    ]
