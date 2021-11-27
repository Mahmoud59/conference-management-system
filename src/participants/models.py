from django.contrib.auth.models import User
from django.db import models

from talks.models import Talk


class Participant(User):
    is_speaker = models.BooleanField("Is Speaker", default=0)
    talk = models.ForeignKey(Talk, on_delete=models.SET_NULL,
                             null=True, related_name="speaker_talk")
