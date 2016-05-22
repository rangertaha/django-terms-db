# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework import routers

from .views import TermViewDetail, TermViewList, TermAPIViewSet, CategoryAPIViewSet

router = routers.DefaultRouter()
router.register(r'terms', TermAPIViewSet)



urlpatterns = [
    url(r'^api/', include(router.urls)),

    url(r'^$', TermViewList.as_view(), name='term-list'),
    url(r'^(?P<slug>.*)$', TermViewDetail.as_view(), name='term-detail'),




]



