"""Captures views."""
import logging

# Django REST framework
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Models
from hefesto_be.fire.captures.models import Capture
# Serializers
from hefesto_be.fire.captures.serializers import CaptureSerializer

logger = logging.getLogger(__name__)


@api_view(['GET', 'POST'])
def capture_list(request):
    """List all captures, or create a new capture."""
    if request.method == 'GET':
        captures = Capture.objects.all()
        serializer = CaptureSerializer(captures, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CaptureSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT'])
def capture_detail(request, pk):
    """Retrieve or update a capture by id."""
    try:
        capture = Capture.objects.get(pk=pk)
        if request.method == 'GET':
            serializer = CaptureSerializer(capture)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = CaptureSerializer(capture, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
    except Capture.DoesNotExist as dne:
        message = f'Capture with id {pk} does not exist. {dne}'
        logger.error(message)
        return Response({'Error': message}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'PUT'])
def camera_calibrate(request, capture_id):
    """Camera calibrate by capture_id"""
    try:
        capture = Capture.objects.get(pk=capture_id)
        if request.method == 'GET':
            serializer = CaptureSerializer(capture)
            serializer.save_calibration(capture, request.data)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = CaptureSerializer(capture, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
    except Capture.DoesNotExist as dne:
        print(f'%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\nQue pasa: Error {dne}')
        message = f'Capture with id {capture_id} does not exist. {dne}'
        logger.error(message)
        return Response({'Error': message}, status=status.HTTP_404_NOT_FOUND)
