from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from conferences.models import Conference
from conferences.serializers import ConferenceSerializer


class ConferenceViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Conference.objects.all().order_by('-created')
    serializer_class = ConferenceSerializer
