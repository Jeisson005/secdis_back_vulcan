"""Detection model."""

# Django
from django.db import models
from model_utils.models import TimeStampedModel, SoftDeletableModel

# Models
from ..detection_models.models import DetectionModel
from ..labels.models import Label
from ..captures.models import Capture


class Detection(TimeStampedModel, SoftDeletableModel):
    """Detection model.
    A detection is the data resulting of processing an image, a video
    or a frame in real time with a Object Detector.
    """
    file_name = models.CharField(
        'detection file name',
        max_length=100,
        null=True
    )
    file_path = models.TextField('detection file path', null=True)
    processing_date = models.DateTimeField('processing date', null=True)
    safe_count = models.IntegerField('safe count', null=True)
    low_risk_count = models.IntegerField('safe count', null=True)
    high_risk_count = models.IntegerField('safe count', null=True)
    detection_metrics = models.JSONField('detection metrics', null=True)
    other_metrics = models.JSONField('other metrics', null=True)
    detection_model = models.ForeignKey(DetectionModel,
                                        on_delete=models.CASCADE,
                                        null=True)
    capture = models.ForeignKey(Capture, on_delete=models.CASCADE, null=True)

    def __str__(self):
        """Return file name."""
        return self.file_name


class DetectionLabel(TimeStampedModel, SoftDeletableModel):
    """DetectionLabel model."""
    safe_count = models.PositiveSmallIntegerField(null=True)
    low_risk_count = models.PositiveSmallIntegerField(null=True)
    high_risk_count = models.PositiveSmallIntegerField(null=True)
    other_metrics = models.JSONField(null=True)

    # References other models, many-to-many relationship
    label = models.ForeignKey(Label, on_delete=models.CASCADE)
    detection = models.ForeignKey(Detection, on_delete=models.CASCADE)
