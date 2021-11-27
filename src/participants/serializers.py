from rest_framework import serializers

from participants.models import Participant


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'
        extra_kwargs = {
            'talk': {'required': True}
        }
