"""Label serializers."""

# Django REST framework
from rest_framework import serializers

# Models
from .models import Label
from ..detection_models.models import DetectionModel


class LabelSerializer(serializers.ModelSerializer):
    """Label serializers."""

    name = serializers.CharField(max_length=30)

    def create(self, validated_data):
        """Create Label."""
        return Label.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

    class Meta:
        model = Label
        fields = '__all__'
