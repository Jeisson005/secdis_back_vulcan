"""MultimediaType model."""

# Django
from django.db import models
from model_utils.models import TimeStampedModel, SoftDeletableModel


class MultimediaType(TimeStampedModel, SoftDeletableModel):
    """MultimediaType model."""
    name = models.CharField('multimedia type name', max_length=30, unique=True)

    def __str__(self):
        """Return multimedia type name."""
        return self.name

    class Meta:
        """Meta option."""
        ordering = ['name']
