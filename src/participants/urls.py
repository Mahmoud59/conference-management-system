from django.urls.conf import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import TokenObtainPairView

from participants.api import ParticipantViewSet

participant_list = ParticipantViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

participant_detail = ParticipantViewSet.as_view({
    'put': 'update',
    'patch': 'partial_update',
})

urlpatterns = format_suffix_patterns([
    path('participants/login/', TokenObtainPairView.as_view(),
         name='participants-login'),

    path('talks/<int:talk_id>/participants/', participant_list,
         name='participants-list'),
    path('participants/<int:pk>/', participant_detail,
         name='participants-detail'),
])
