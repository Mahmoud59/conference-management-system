import datetime

from django.core.validators import MinValueValidator
from django.db import models
from django_extensions.db.models import TimeStampedModel


class Conference(TimeStampedModel):
    title = models.CharField("Title", max_length=100)
    description = models.TextField("Description")
    start_date = models.DateField("Start Date", validators=[MinValueValidator(
        limit_value=datetime.date.today)])
    end_date = models.DateField("End Date", validators=[MinValueValidator(
        limit_value=datetime.date.today() + datetime.timedelta(days=1))])
