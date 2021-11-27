from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from talks.models import Talk
from talks.serializers import TalkSerializer


class TalkViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Talk.objects.all().order_by('-created')
    serializer_class = TalkSerializer

    def get_queryset(self):
        if self.kwargs.get('conference_id', None):
            return self.queryset.filter(
                conference=self.kwargs['conference_id'])
        return self.queryset

    def create(self, request, *args, **kwargs):
        request.data['conference'] = kwargs['conference_id']
        talk_serializer = self.serializer_class(data=request.data)
        talk_serializer.is_valid(raise_exception=True)
        talk_serializer.save()
        return Response(talk_serializer.data, status=status.HTTP_201_CREATED)
