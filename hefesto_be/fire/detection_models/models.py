"""DetectionModel model."""

# Django
from django.conf import settings
from django.db import models
from model_utils.models import TimeStampedModel, SoftDeletableModel

# Models
from hefesto_be.fire.labels.models import Label


class DetectionModel(TimeStampedModel, SoftDeletableModel):
    """DetectionModel model.
    A detection model refers to a object detector model.
    """

    name = models.CharField('detection model name', max_length=300)
    configuration_file_path = models.FileField(
        storage=settings.FILE_STORAGE, blank=False, null=False)
    weight_file_path = models.FileField(
        storage=settings.FILE_STORAGE, blank=False, null=False)
    class_file_path = models.FileField(
        storage=settings.FILE_STORAGE, blank=False, null=False)
    labels = models.ManyToManyField(Label, blank=False)
