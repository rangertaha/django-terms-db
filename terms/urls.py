from django.urls import include, path, re_path
from rest_framework import routers

from .views import TermViewAlphabetList, TermViewList, TermViewDetail, TermAPIViewSet

router = routers.DefaultRouter()
router.register(r'terms', TermAPIViewSet)


urlpatterns = [
    path('api/', include(router.urls)),

    path('', TermViewList.as_view(), name='term-list'),
    re_path(r'^(?P<alphabet>\D)$', TermViewAlphabetList.as_view(), name='term-alphabet-list'),
    re_path(r'^detail/(?P<pk>\d+)/(.*)$', TermViewDetail.as_view(), name='term-detail'),
]
