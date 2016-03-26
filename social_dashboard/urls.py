# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from .views import social_dashboard, social_dashboard_twitter

urlpatterns = [
    url(r'^$', social_dashboard, name="dashboard_index"),
    url(r'twitter/', social_dashboard_twitter, name="dashboard_twitter"),
]
