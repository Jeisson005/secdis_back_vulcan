"""Labels views."""

# Django REST framework
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Models
from hefesto_be.fire.labels.models import Label
# Serializers
from hefesto_be.fire.labels.serializers import LabelSerializer


@api_view(['GET', 'POST'])
def label_list(request):
    """List all labels, or create a new label"""
    try:
        if request.method == 'GET':
            labels = Label.objects.all()
            serializer = LabelSerializer(labels, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = LabelSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as ex:
        return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)


@api_view(['GET', 'PUT'])
def label_detail(request, pk):
    """Retrieve or update a label by id."""
    try:
        label = Label.objects.get(pk=pk)
        if request.method == 'GET':
            serializer = LabelSerializer(label)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = LabelSerializer(label, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
    except Label.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
