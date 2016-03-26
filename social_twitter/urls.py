# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from .views import social_twitter_fetch

urlpatterns = [
    url(r'twitter_fetch/', social_twitter_fetch, name="twitter_fetch_latest"),
]
