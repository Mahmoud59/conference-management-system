from django.urls.conf import path
from rest_framework.urlpatterns import format_suffix_patterns

from conferences.api import ConferenceViewSet

conference_list = ConferenceViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

conference_detail = ConferenceViewSet.as_view({
    'put': 'update',
    'patch': 'partial_update',
})

urlpatterns = format_suffix_patterns([
    path('conferences/', conference_list,
         name='conferences-list'),
    path('conferences/<int:pk>/', conference_detail,
         name='conferences-detail'),
])
