"""Label model."""

# Django
from django.db import models
from model_utils.models import TimeStampedModel, SoftDeletableModel

# Models


class Label(TimeStampedModel, SoftDeletableModel):
    """Label model."""

    name = models.CharField('label name', max_length=30, unique=True)
