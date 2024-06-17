"""Detections serializers."""

# Django REST framework
from rest_framework import serializers

# Models
from hefesto_be.fire.captures.models import Capture
from hefesto_be.fire.detection_models.models import DetectionModel
from hefesto_be.fire.detections.models import Detection


class DetectionSerializer(serializers.ModelSerializer):
    """Detections serializers."""
    file_name = serializers.CharField(allow_null=True, allow_blank=True)
    file_path = serializers.CharField(allow_null=True, allow_blank=True)
    processing_date = serializers.DateTimeField(allow_null=True)
    safe_count = serializers.IntegerField(allow_null=True)
    low_risk_count = serializers.IntegerField(allow_null=True)
    high_risk_count = serializers.IntegerField(allow_null=True)
    detection_metrics = serializers.JSONField(allow_null=True, required=False)
    other_metrics = serializers.JSONField(allow_null=True, required=False)
    detection_model = serializers.PrimaryKeyRelatedField(
        queryset=DetectionModel.objects.all()
    )
    capture = serializers.PrimaryKeyRelatedField(
        queryset=Capture.objects.all()
    )

    def create(self, validated_data):
        """Create Detection."""
        return Detection.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """Update Detection"""
        instance.file_name = validated_data.get('file_name',
                                                instance.file_name)
        instance.file_path = validated_data.get('file_path',
                                                instance.file_path)
        instance.processing_date = validated_data.get(
            'processing_date', instance.processing_date)
        instance.safe_count = validated_data.get('safe_count',
                                                 instance.safe_count)
        instance.low_risk_count = validated_data.get('low_risk_count',
                                                     instance.low_risk_count)
        instance.high_risk_count = validated_data.get(
            'high_risk_count', instance.high_risk_count)
        instance.detection_metrics = validated_data.get(
            'detection_metrics', instance.detection_metrics)
        instance.other_metrics = validated_data.get(
            'other_metrics', instance.other_metrics)
        instance.detection_model = validated_data.get(
            'detection_model', instance.detection_model)
        instance.capture = validated_data.get('capture', instance.capture)
        instance.save()
        return instance

    class Meta:
        model = Detection
        fields = '__all__'
