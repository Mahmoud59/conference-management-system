from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from participants.models import Participant
from participants.serializers import ParticipantSerializer


class ParticipantViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer

    def get_queryset(self):
        return self.queryset.filter(talk=self.kwargs['talk_id'])

    def create(self, request, *args, **kwargs):
        request.data['talk'] = kwargs['talk_id']
        participant_serializer = self.serializer_class(data=request.data)
        participant_serializer.is_valid(raise_exception=True)
        participant_serializer.save()
        return Response(participant_serializer.data,
                        status=status.HTTP_201_CREATED)
