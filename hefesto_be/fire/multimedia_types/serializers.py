"""MultimediaType serializers."""

# Django REST framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Models
from hefesto_be.fire.multimedia_types.models import MultimediaType


class MultimediaTypeSerializer(serializers.ModelSerializer):
    """MultimediaType serializers."""
    name = serializers.CharField(
        validators=[
            UniqueValidator(queryset=MultimediaType.objects.all())
        ]
    )

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        """Create MutlimediaType."""
        return MultimediaType.objects.create(**validated_data)

    class Meta:
        model = MultimediaType
        fields = '__all__'
