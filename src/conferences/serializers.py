from rest_framework import serializers

from conferences.models import Conference


class ConferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conference
        fields = '__all__'
