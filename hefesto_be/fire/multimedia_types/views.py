"""MultimediaTypes views."""

# Django REST framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Models
from hefesto_be.fire.multimedia_types.models import MultimediaType

# Serializers
from hefesto_be.fire.multimedia_types.serializers import MultimediaTypeSerializer


@api_view(['GET', 'POST', 'PUT'])
def multimedia_type(request):
    """Create, uptade and list multimedia type."""
    if request.method == 'GET':
        multimedia_types = MultimediaType.objects.all()
        serializer = MultimediaTypeSerializer(multimedia_types, many=True)
    elif request.method == 'POST':
        serializer = MultimediaTypeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_multimedia_type = serializer.save()
        serializer = MultimediaTypeSerializer(new_multimedia_type)
    elif request.method == 'PUT':
        return Response("Error: Estamos implementando la función.",
                        status=404)
    else:
        return Response("Error: Método no valido.", status=404)
    return Response(serializer.data)
