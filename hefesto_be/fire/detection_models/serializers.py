"""MultimediaType serializers."""

# Django REST framework
from rest_framework import serializers

# Models
from hefesto_be.fire.detection_models.models import DetectionModel


class DetectionModelSerializer(serializers.ModelSerializer):
    """DetectionModel serializers."""
    name = serializers.CharField(max_length=300)
    configuration_file_path = serializers.FileField(
        allow_empty_file=False,
        use_url=True
    )
    weight_file_path = serializers.FileField(allow_empty_file=False)
    class_file_path = serializers.FileField(allow_empty_file=False)

    def create(self, validated_data):
        """Create DetectionModel."""
        labels = validated_data.pop('labels', None)
        new_detection_model = DetectionModel.objects.create(**validated_data)
        new_detection_model.labels.set(labels)
        return new_detection_model

    def update(self, instance, validated_data):
        """Update DetectionModel."""
        instance.name = validated_data.get('name', instance.name)
        instance.configuration_file_path = validated_data.get(
            'configuration_file_path', instance.configuration_file_path)
        instance.weight_file_path = validated_data.get(
            'weight_file_path', instance.weight_file_path)
        instance.class_file_path = validated_data.get(
            'class_file_path', instance.class_file_path)
        instance.labels.set(validated_data.get(
            'labels', instance.labels))
        instance.save()
        return instance

    class Meta:
        model = DetectionModel
        fields = '__all__'
        ordering = ['id']
