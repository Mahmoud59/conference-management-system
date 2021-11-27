from rest_framework import serializers

from talks.models import Talk


class TalkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talk
        fields = '__all__'
        extra_kwargs = {
            'conference': {'required': True},
            'speaker': {'required': True}
        }
