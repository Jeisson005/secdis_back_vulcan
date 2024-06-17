"""Capture model."""
import logging
from io import BytesIO

# Django
from django.core.files.base import ContentFile
from django.db import models
from model_utils.models import TimeStampedModel, SoftDeletableModel

from hefesto_be.fire.labels.models import Label
# Models
from hefesto_be.fire.multimedia_types.models import MultimediaType
# utils
from hefesto_be.fire.utils.utils import get_frame, get_int_timestamp

logger = logging.getLogger(__name__)


def capture_image_path(instance, filename):
    return f'capture_{instance.name}/calibration_images/{filename}'


def distance_calibration_metric():
    return dict({'safe_low_risk_radius': 200,
                 'low_high_risk_radius': 150})


class Capture(TimeStampedModel, SoftDeletableModel):
    """Capture model.
    A capture refers to a media file (image, video, real-time capture),
    it also stores metadata ().
    """

    name = models.CharField('capture name', max_length=100)
    path = models.TextField(
        'file path or camera url',
        help_text=(
            'This value can be one number (device index, is just '
            'the number to specify which camera), or url camera, '
            'or name of a video/image file (file path).'
        )
    )

    # Coordinates where the videos or images were taken, or where the
    # cameras are located
    latitude = models.CharField(
        'capture latitude',
        max_length=30,
        blank=True,
        null=True,
        help_text=(
            'Latitude where the videos or images were taken, '
            'or where the cameras are located.')
    )
    longitude = models.CharField(
        'capture longitude',
        max_length=30,
        blank=True,
        null=True,
        help_text=(
            'Longitude where the videos or images were taken, '
            'or where the cameras are located.')
    )

    capture_date = models.DateTimeField(
        'capture date', blank=True, null=True,
        auto_now_add=True
    )
    calibr_image_name = models.CharField(
        'camera calibration image name',
        default=(str(get_int_timestamp()) + '.PNG'),
        max_length=255,
        null=True,
        help_text=(
            'Camera calibration image name'
        )
    )
    calibr_image_path = models.ImageField(
        'camera calibration image path',
        blank=True,
        null=True,
        upload_to=capture_image_path,
        help_text=(
            'Camera calibration image path'
        )
    )
    dist_calibr_metric = models.JSONField(
        'distance calibration metric in cm (radius)',
        default=distance_calibration_metric,
        null=True)
    image_size = models.JSONField('calibration image size or video frames, '
                                  '{ width: value, height: value}', null=True)
    points = models.JSONField('points data, { point: { '
                              'center: { x: value, y: value}, '
                              'vertical: { x: value, y: value}, '
                              'horizontal: { x: value, y: value}},'
                              'rectangle: [{ x: value, y: value},'
                              '{ x: value, y: value}, { x: value, y: value},'
                              '{ x: value, y: value}]}', null=True)
    other = models.JSONField('other data', null=True)

    # References another model, one-to-many relationship
    multimedia_type = models.ForeignKey(MultimediaType, on_delete=models.CASCADE)
    filter_labels = models.ManyToManyField(Label, blank=False)

    def __str__(self):
        """Return name."""
        return self.name

    def save_calibration(self, *args, **kwargs):
        if self.path != '':
            try:
                img, size = get_frame(self.path)
                if img:
                    filename = self.calibr_image_name
                    self.calibr_image_path = filename
                    tempfile = img
                    tempfile_io = BytesIO()
                    tempfile.save(tempfile_io, format='PNG')
                    self.calibr_image_path.save(
                        filename,
                        ContentFile(tempfile_io.getvalue()),
                        save=False)
                    self.image_size = size

            except Exception as e:
                logger.error(f'Calibration could not be saved. Error:{e}')
        super(Capture, self).save(*args, **kwargs)

    class Meta:
        """Meta option."""
        ordering = ['pk']
