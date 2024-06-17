"""Capture serializers."""

# Django REST framework
from rest_framework import serializers

# Models
from hefesto_be.fire.captures.models import Capture
from hefesto_be.fire.multimedia_types.models import MultimediaType


class CaptureSerializer(serializers.ModelSerializer):
    """Capture serializers."""
    name = serializers.CharField(max_length=100)
    path = serializers.CharField()
    latitude = serializers.CharField(
        max_length=30, allow_blank=True, allow_null=True
    )
    longitude = serializers.CharField(
        max_length=30, allow_blank=True, allow_null=True
    )
    capture_date = serializers.DateTimeField(
        format='iso-8601',
        allow_null=True,
        required=False
    )
    calibr_image_name = serializers.CharField(allow_null=True, required=False)
    calibr_image_path = serializers.ImageField(allow_null=True, required=False)
    dist_calibr_metric = serializers.JSONField(allow_null=True, required=False)
    image_size = serializers.JSONField(allow_null=True, required=False)
    points = serializers.JSONField(allow_null=True, required=False)
    other = serializers.JSONField(allow_null=True, required=False)
    multimedia_type = serializers.PrimaryKeyRelatedField(
        queryset=MultimediaType.objects.all()
    )

    def create(self, validated_data):
        """Create Capture."""
        filter_labels = validated_data.pop('filter_labels', None)
        new_capture = Capture.objects.create(**validated_data)
        new_capture.filter_labels.set(filter_labels)
        return new_capture

    def update(self, instance, validated_data):
        """Update Capture."""
        instance.name = validated_data.get('name', instance.name)
        instance.path = validated_data.get('path', instance.path)
        instance.latitude = validated_data.get('latitude', instance.latitude)
        instance.longitude = validated_data.get('longitude', instance.longitude)
        instance.capture_date = validated_data.get('capture_date',
                                                   instance.capture_date)
        instance.calibr_image_name = validated_data.get('calibr_image_name',
                                                        instance.calibr_image_name)
        instance.calibr_image_path = validated_data.get('calibr_image_path',
                                                        instance.calibr_image_path)
        instance.dist_calibr_metric = validated_data.get('dist_calibr_metric',
                                                         instance.dist_calibr_metric)
        instance.image_size = validated_data.get('image_size', instance.image_size)
        instance.points = validated_data.get('points', instance.points)
        instance.multimedia_type = validated_data.get(
            'multimedia_type',
            instance.multimedia_type
        )
        if 'filter_labels' in validated_data:
            instance.filter_labels.set(validated_data.get('filter_labels',
                                                          instance.filter_labels))
        instance.save()
        return instance

    def save_calibration(self, instance, validated_data):
        instance.calibr_image_path = validated_data.get('calibr_image_path',
                                                        instance.calibr_image_path)
        instance.save_calibration()
        return instance

    class Meta:
        model = Capture
        fields = '__all__'
        ordering = ['id']
