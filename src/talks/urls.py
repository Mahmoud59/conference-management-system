from django.urls.conf import path
from rest_framework.urlpatterns import format_suffix_patterns

from talks.api import TalkViewSet

talk_list = TalkViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

talk_detail = TalkViewSet.as_view({
    'put': 'update',
    'patch': 'partial_update',
})

urlpatterns = format_suffix_patterns([
    path('conferences/<int:conference_id>/talks/', talk_list,
         name='talks-list'),
    path('talks/<int:pk>/', talk_detail,
         name='talks-detail'),
])
