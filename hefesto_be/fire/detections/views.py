"""Detections views.

For more information about ViewSets, see
https://www.django-rest-framework.org/api-guide/viewsets/

For more information about Routers, see
https://www.django-rest-framework.org/api-guide/routers/

For more information about ViewSets and Routers, see
https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/
"""

from django_filters.rest_framework import DjangoFilterBackend
# Django REST framework
from rest_framework import viewsets

# Models
from hefesto_be.fire.detections.models import Detection
# Serializers
from hefesto_be.fire.detections.serializers import DetectionSerializer


class DetectionViewSet(viewsets.ModelViewSet):
    """Detection View Set"""
    queryset = Detection.objects.all()
    serializer_class = DetectionSerializer
    http_method_names = ['get', 'post', 'put', 'patch']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['capture_id']
