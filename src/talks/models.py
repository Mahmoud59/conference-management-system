from django.db import models
from django_extensions.db.models import TimeStampedModel

from conferences.models import Conference


class Talk(TimeStampedModel):
    title = models.CharField("Title", max_length=100)
    description = models.TextField("Description")
    duration = models.DurationField("Duration")
    date = models.DateTimeField("Date")
    conference = models.ForeignKey(Conference, on_delete=models.SET_NULL,
                                   null=True, related_name="talk_conference")
