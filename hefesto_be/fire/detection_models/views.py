"""DetectionModels views."""
import logging

# Django REST framework
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Models
from hefesto_be.fire.detection_models.models import DetectionModel
# Serializers
from hefesto_be.fire.detection_models.serializers import DetectionModelSerializer

logger = logging.getLogger(__name__)


@api_view(['GET', 'POST'])
def detection_model_list(request):
    """List all detection models, or create a new detection model."""
    if request.method == 'GET':
        detection_models = DetectionModel.objects.all()
        serializer = DetectionModelSerializer(detection_models, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DetectionModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT'])
def detection_model_detail(request, pk):
    """Retrieve or update a detection model by id."""
    try:
        detection_model = DetectionModel.objects.get(pk=pk)
        if request.method == 'GET':
            serializer = DetectionModelSerializer(detection_model)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = DetectionModelSerializer(detection_model,
                                                  data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
    except DetectionModel.DoesNotExist as dne:
        message = f'Detection Model with id {pk} does not exist. {dne}'
        logger.error(message)
        return Response({'Error': message}, status=status.HTTP_404_NOT_FOUND)
