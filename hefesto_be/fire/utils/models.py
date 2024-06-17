"""Django models utilities."""

# Django
from django.db import models


class BaseModel(models.Model):
    """Base model.

    BaseModel acts as an abstract base class from which every
    other model in the project will inherit. This class provides
    every table with the following attributes:
        + created_at (DateTime): Store the datetime the object was created.
        + modified_at (DateTime): Store the last datetime the object was modified.
    """

    created_at = models.DateTimeField(
        'created_at',
        auto_now_add=True,
        help_text='Date time on which the object was created.'
    )

    modified_at = models.DateTimeField(
        'modified_at',
        auto_now=True,
        help_text='Date time on which the object was last modified.'
    )

    class Meta:
        """Meta option."""
        abstract = True

        get_latest_by = 'created_at'
        ordering = ['-created_at', '-modified_at']
